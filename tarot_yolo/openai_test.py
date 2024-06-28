import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="sk-eqMhRPBcaKFzTFSm5DrCwLiQ9baLRpwP",
    base_url="https://api.proxyapi.ru/openai/v1"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "You are a tarologist. You have to explain the 3 cards spread. The order is the following: 1. You 2. Dynamic 3.Partner. The cards given: 1. fool, 2. pentacles-10, 3. swords-queen",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)