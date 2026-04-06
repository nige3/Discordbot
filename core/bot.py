# Factory function to create and configure the Discord bot instance
import discord
from discord.ext import commands
from config import PREFIX

def create_bot():
    # Set up intents to enable specific gateway events
    intents = discord.Intents.default()
    intents.message_content = True  # Read message content from events
    intents.members = True  # Track member join/leave events

    # Create bot with specified prefix and intents configuration
    bot = commands.Bot(
        command_prefix=PREFIX,
        intents=intents
    )

    return bot