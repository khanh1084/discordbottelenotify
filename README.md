# Discord to Telegram Bot

This project is a bot that forwards messages from specified Discord channels to a Telegram chat.

## Prerequisites

Make sure you have the following installed:

-   Python 3.6+
-   pip (Python package installer)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/khanh1084/discordbottelenotify
    cd discord-to-telegram-bot
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file by copying the `.env.example` file and filling in your credentials:

    ```sh
    cp .env.example .env
    ```

    Edit the `.env` file and replace the placeholders with your actual tokens and IDs:

    ```env
    DISCORD_TOKEN=your_discord_token_here
    TELEGRAM_TOKEN=your_telegram_token_here
    TELEGRAM_CHAT_ID=your_telegram_chat_id_here
    DISCORD_CHANNEL_IDS=channel_id_1,channel_id_2,channel_id_3
    ```

## Usage

Run the bot with the following command:

```sh
python run.py
```

## Dependencies

The project uses the following libraries:

discord.py: Python wrapper for the Discord API.
python-telegram-bot: Python wrapper for the Telegram Bot API.
python-dotenv: Reads key-value pairs from a .env file and can set them as environment variables.
