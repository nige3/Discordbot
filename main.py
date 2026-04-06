# Import async utilities and core modules needed for Discord bot initialization and management
import asyncio
import os
from core.bot import create_bot
from config import TOKEN
from core.events import setup_events
from core.errors import setup_errors

# Initialize the bot instance from our custom factory function
bot = create_bot()

# Register event handlers and error handling middleware to the bot
setup_events(bot)
setup_errors(bot)

# Responds to the ping slash command with a pong emoji
@bot.tree.command(name="ping")
async def slash_ping(interaction):
    await interaction.response.send_message("🏓 Pong !")

# Template for adding more slash commands
# @bot.tree.command(name="command_name")
# async def slash_command_name(interaction):
#     await interaction.response.send_message("Response")

# Dynamically loads all Python files from the cogs directory
async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")

# Main entry point that starts the bot with loaded cogs and event handlers
async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

# Run the async main function to start the bot
asyncio.run(main())