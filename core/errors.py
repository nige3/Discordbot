# Handle errors gracefully so users get helpful feedback
from discord.ext import commands

def setup_errors(bot):

    # When something goes wrong, we'll let the user know what happened
    @bot.event
    async def on_command_error(ctx, error):
        # Oops, you don't have permission for that
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ Looks like you don't have permission to do that!")
        # Command doesn't exist, but let's stay quiet about it
        elif isinstance(error, commands.CommandNotFound):
            pass
        # Something unexpected happened, let's tell them
        else:
            await ctx.send(f"⚠️ Oops! Something went wrong: {error}")