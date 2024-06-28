# from ultralytics import YOLO
# import cv2

# model = YOLO('tarot_yolo/models/tarot_yolov9.pt')
# results = model.predict(source="0", show=True)

import sys
import logging
import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.types import ContentType
from aiogram import F
from ultralytics import YOLO
import cv2
import numpy as np
from io import BytesIO
from PIL import Image
from dotenv import dotenv_values
from openai import OpenAI
import json

config = dotenv_values(".env")

print(config)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
API_TOKEN = config['API_TOKEN']
OPEANAI_API_TOKEN = config['OPENAI_API_TOKEN']
dp = Dispatcher()
router = Router()

# Initialize the YOLO model
model = YOLO('tarot_yolo/models/tarot_yolov9.pt')
client = OpenAI(
    # This is the default and can be omitted
    api_key=OPEANAI_API_TOKEN,
    base_url="https://api.proxyapi.ru/openai/v1" # For usage from Russian Federation
)

#@router.message(CommandStart())
@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Hi! Send me an image of a tarot layout, and I'll recognize the cards for you.")

@dp.message(F.photo)
async def handle_photo(message: types.Message):
    photo = message.photo[-1]  # Get the highest resolution photo
    print(photo.file_id)
    photo_file = await message.bot.download(file=photo.file_id, destination=BytesIO())
    photo_file.seek(0)
    
    # Convert to OpenCV format
    img = Image.open(photo_file)
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    # Perform prediction using the YOLO model
    results = model.predict(source=img, save=True)
    
    # Process results
    cards_detected = []
    for result in results:
        for box in result.boxes:
            cls = box.cls.item()
            score = box.conf.item()
            x_min, y_min, x_max, y_max = box.xyxy.tolist()[0]  # Extract the coordinates
            label = model.names[int(cls)]
            cards_detected.append((label, score, x_min, y_min))
    
    # Sort cards by y-coordinate (top to bottom) first, then by x-coordinate (left to right)
    cards_detected.sort(key=lambda x: (x[3], x[2]))
    
    # Remove duplicates while maintaining order
    seen = set()
    unique_cards_detected = []
    for card in cards_detected:
        if card[0] not in seen:
            unique_cards_detected.append(card)
            seen.add(card[0])
    
    # Create response message
    if unique_cards_detected:
        response_message = ""
        for card, score, _, _ in unique_cards_detected:
            response_message += f"{card}, "# (confidence: {score:.2f})\n"
    else:
        response_message = "I couldn't recognize any cards in the image."
    
    await message.answer(f"Detected cards: {response_message}\nNow I'll explain the layout...")

    output = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"You are a tarologist. You have to explain the 3 cards spread. The order is the following: 1. You 2. Dynamic 3.Partner. The cards given in order are {response_message}",
            }
        ],
        model="gpt-3.5-turbo",
    )
    await message.answer(output.choices[0].message.content)

async def main() -> None:
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
