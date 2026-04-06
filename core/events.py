# Sets up all the event handlers that make the bot come alive
def setup_events(bot):

    # When we successfully connect to Discord, let's say hello
    @bot.event
    async def on_ready():
        print(f"🤖 I'm awake! Logged in as {bot.user}")

    # Give new members a warm welcome when they join
    @bot.event
    async def on_member_join(member):
        if member.guild.system_channel:
            await member.guild.system_channel.send(
                f"Welcome to the server, {member.mention}! 👋 Excited to have you here!"
            )

    # Listen to messages and react to commands
    @bot.event
    async def on_message(message):
        # Don't talk to other bots (that gets messy)
        if message.author.bot:
            return

        # Process any commands in the message
        await bot.process_commands(message)