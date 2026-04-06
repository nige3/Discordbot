# Keep the server safe with moderation tools
from discord.ext import commands

class Moderation(commands.Cog):
    """Tools to manage members and keep the server running smoothly"""
    def __init__(self, bot):
        self.bot = bot

    # Remove someone from the server (temporarily)
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"👢 {member} has been kicked from the server.")

    # Permanently remove someone from the server
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"🔨 {member} is banned. They won't be coming back.")

    # Give someone a warning for breaking rules
    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def warn(self, ctx, member, *, reason="No reason provided"):
    #     """Let someone know they're breaking the rules"""
    #     await ctx.send(f"⚠️ {member} has been warned: {reason}")

    # Temporarily prevent someone from talking
    # @commands.command()
    # @commands.has_permissions(manage_roles=True)
    # async def mute(self, ctx, member, *, reason="No reason provided"):
    #     """Silence a problematic user"""
    #     await ctx.send(f"🔇 {member} has been muted: {reason}")

# Load the moderation commands
async def setup(bot):
    await bot.add_cog(Moderation(bot))