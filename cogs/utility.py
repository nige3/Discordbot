# Utility commands for retrieving server and user information
import discord
from discord.ext import commands

class Utility(commands.Cog):
    """Information and utility commands"""
    def __init__(self, bot):
        self.bot = bot

    # Displays server statistics in an embedded message
    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title=guild.name)
        embed.add_field(name="Members", value=guild.member_count)
        await ctx.send(embed=embed)

    # Template for user info command
    # @commands.command()
    # async def userinfo(self, ctx, member=None):
    #     """Get information about a user"""
    #     member = member or ctx.author
    #     embed = discord.Embed(title=f"User Info: {member}")
    #     embed.add_field(name="ID", value=member.id)
    #     embed.add_field(name="Joined", value=member.joined_at)
    #     await ctx.send(embed=embed)

# Required setup function to load this cog into the bot
async def setup(bot):
    await bot.add_cog(Utility(bot))