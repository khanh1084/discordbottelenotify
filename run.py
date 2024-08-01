import discord
from telegram import Bot
from dotenv import load_dotenv, find_dotenv
import os
import asyncio

# Load environment variables from .env file
dotenv_path = find_dotenv()
print(f'Loading .env from: {dotenv_path}')
load_dotenv(dotenv_path)
load_dotenv()

# Discord bot token
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
print(f'DISCORD_TOKEN: {DISCORD_TOKEN}')
# Telegram bot token
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
# Telegram chat ID
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
# List of Discord channel IDs to monitor
discord_channel_ids = os.getenv('DISCORD_CHANNEL_IDS')
DISCORD_CHANNEL_IDS = discord_channel_ids.split(',') if discord_channel_ids else []

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent if needed

client = discord.Client(intents=intents)
telegram_bot = Bot(token=TELEGRAM_TOKEN)

message_queue = asyncio.Queue()
message_buffer = []

async def send_telegram_messages():
    while True:
        await asyncio.sleep(1)  # Wait for 1 second
        if not message_queue.empty():
            combined_message = []
            while not message_queue.empty():
                combined_message.append(await message_queue.get())
            combined_message = "\n".join(combined_message)
            try:
                await telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=combined_message)
            except Exception as e:
                print(f"Error sending message: {e}")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    asyncio.create_task(send_telegram_messages())

@client.event
async def on_message(message):
    # Check if the message is from the bot to avoid infinite loop
    if message.author == client.user:
        return

    # Check if the message is from the registered channels
    if str(message.channel.id) in DISCORD_CHANNEL_IDS:
        print(f'Message from {message.guild.name} in {message.channel.name}: {message.content}')
        
        # Add the message to the queue and buffer
        telegram_message = f'Message from {message.guild.name} in {message.channel.name}: {message.content}'
        await message_queue.put(telegram_message)
        message_buffer.append(telegram_message)

client.run(DISCORD_TOKEN)