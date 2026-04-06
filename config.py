# Configuration module for loading bot settings from environment variables
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Discord bot token from environment (required for running the bot)
TOKEN = os.getenv("DISCORD_TOKEN")
# Command prefix for text-based commands (e.g., !ping)
PREFIX = "!"