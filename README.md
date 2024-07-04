# 🔮 Tarot YOLO Bot 🤖
<i>Telegram bot which tells your future</i>

Welcome to **Tarot YOLO Bot**, a cutting-edge Telegram bot that blends the power of YOLOv9n for tarot card recognition and ChatGPT 3.5 Turbo for explaining tarot spreads. Dive into the world of tarot with AI-assisted insights! 🌟

| :exclamation:|  YOLOv9 was trained on a classic Waite's 78 cards deck, others not supported yet!   |
|--------------|:------------------------------------------------------------------------------------|

## Features ✨

- **Tarot Card Recognition** 🃏: Leveraging YOLOv9n to identify and interpret tarot cards.
- **AI-Powered Explanations** 🧠: ChatGPT 3.5 Turbo provides detailed insights and explanations of tarot spreads.
- **Seamless Integration** 📱: Easy to use within Telegram, offering a smooth user experience.
- **Modern Development Setup** 🛠️: Built with Poetry for dependency management and includes a Dockerfile for containerization.

## Getting Started 🚀

### Prerequisites 📋

- Python 3.8+
- [Poetry](https://python-poetry.org/docs/#installation)
- Docker (optional, for containerization)

### Installation 🛠️

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ivanovsdesign/tarot_yolo.git
    cd tarot_yolo
    ```

2. **Install dependencies** using Poetry:
    ```bash
    poetry install
    ```

3. **Set up environment variables**:
    - Create a `.env` file in the root directory.
    - Add your Telegram bot token and OpenAI API key:
      ```env
      API_TOKEN=your_telegram_bot_token
      OPENAI_API_TOKEN=your_openai_api_key
      ```

### Usage 🏃

To run the bot locally, execute:
```bash
poetry run python tarot_yolo
