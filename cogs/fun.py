# Fun and entertainment commands for server enjoyment
import random
from discord.ext import commands

class Fun(commands.Cog):
    """Entertainment and game-related commands"""
    def __init__(self, bot):
        self.bot = bot

    # Rolls a dice and returns random number from 1 to 6
    @commands.command()
    async def roll(self, ctx):
        await ctx.send(f"Dice rollin'.... {random.randint(1,6)}")

    # Template for fortune telling command
    # @commands.command()
    # async def fortune(self, ctx):
    #     """Get a random fortune"""
    #     fortunes = ["Good luck!", "Be bold!", "You will succeed!"]
    #     await ctx.send(random.choice(fortunes))

    # Template for flip coin command
    # @commands.command()
    # async def flip(self, ctx):
    #     """Flip a coin and get heads or tails"""
    #     result = random.choice(["Heads", "Tails"])
    #     await ctx.send(f"Coin flipped: {result}")

# Required setup function to load this cog into the bot
async def setup(bot):
    await bot.add_cog(Fun(bot))