import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
IMAGE_CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot connected as {client.user}')

@client.event
async def on_message(message):
    # Ignore bot's own messages
    if message.author.bot:
        return

    # Only enforce in the specific channel
    if message.channel.id == IMAGE_CHANNEL_ID:
        if len(message.attachments) == 0:
            await message.delete()
        else:
            # Optional: Only allow image files
            allowed = ['image/png', 'image/jpeg', 'image/gif']
            for attachment in message.attachments:
                if attachment.content_type not in allowed:
                    await message.delete()
                    return

client.run(TOKEN)
