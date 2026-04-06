# Fun and useful commands everyone can use
from discord.ext import commands

class General(commands.Cog):
    """General commands that anyone can use"""
    def __init__(self, bot):
        self.bot = bot

    # Check if I'm alive and responsive
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong! 🏓 I'm here!")

    # Give someone a friendly greeting
    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hey {ctx.author.mention}! What's up? 👋")

    # Use this template to add your own fun commands
    # @commands.command()
    # async def command_name(self, ctx, arg1, arg2=None):
    #     """Do something cool with arguments"""
    #     await ctx.send("Your response here")

# Load this group of commands when the bot starts
async def setup(bot):
    await bot.add_cog(General(bot))