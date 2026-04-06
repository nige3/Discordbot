# Discord Bot Template 🤖

A reusable Discord bot starter project built with `discord.py`.
Use this template to quickly add commands, event handlers, and custom cogs.

## Template Overview

This repo includes:

- `main.py` — bot entry point and startup flow
- `config.py` — loads settings and bot token
- `core/` — shared bot setup, event handlers, and error handling
- `cogs/` — individual feature groups for commands
- `.env` — environment variables (not committed)

## How to Use This Template

1. Copy or fork this repository into your own project.
2. Edit or replace the example commands in `cogs/`.
3. Add your bot token to `.env`.
4. Run the bot with `python main.py`.

## Setup

### Prerequisites

- Python 3.8+
- Discord bot token from the [Discord Developer Portal](https://discord.com/developers)

### Install

```bash
cd Discordbot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configure

Copy or update `.env.example` to create a `.env` file in the root:

```text
DISCORD_TOKEN=your_bot_token_here
```

### Setup helpers

This template also includes helpful setup tools in `setup_tools/`:
- `fix.py` — create missing `.env` and `cogs/`, install required packages
- `troubleshoot.py` — verify dependencies, token, and project structure

### Makefile shortcuts

- `make setup` — create environment and install requirements
- `make fix` — run the fix helper
- `make troubleshoot` — run the troubleshooting helper
- `make run` — start the bot
- `make format` — format code with Black
- `make lint` — check formatting with Black
- `make install-hooks` — install pre-commit hooks

### Pre-commit support

This repo includes `.pre-commit-config.yaml` for formatting and repo hygiene checks.
Install hooks by running:

```bash
make install-hooks
```

### Run

```bash
python main.py
```

## What You Can Customize

### Add a new cog

1. Create a new file in `cogs/`, e.g. `music.py`
2. Add a cog class with commands
3. Use the `async def setup(bot)` loader
4. Restart the bot

### Change the command prefix

Edit `PREFIX` in `config.py`.

### Add slash commands

Add `@bot.tree.command(name="...")` to `main.py` or a cog, then sync commands in your startup flow.

## Example Command Templates

### General command template

```python
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}!")

async def setup(bot):
    await bot.add_cog(Example(bot))
```

### Slash command template

```python
@bot.tree.command(name="hello")
async def slash_hello(interaction):
    await interaction.response.send_message("Hello from a slash command!")
```

## Project Structure

```text
Discordbot/
├── main.py
├── config.py
├── core/
│   ├── bot.py
│   ├── events.py
│   └── errors.py
├── cogs/
│   ├── general.py
│   ├── fun.py
│   ├── utility.py
│   └── moderation.py
├── .env
├── .gitignore
└── README.md
```

## Notes

- Keep your bot token secret.
- Add any new commands to a cog and restart the bot.
- This template is meant to be extended, not used as a finished bot.

## Troubleshooting

- **Bot fails to start**: verify `.env` and `DISCORD_TOKEN`
- **Commands don't work**: check `cogs/` filenames and syntax
- **Slash commands missing**: sync them after startup or restart the bot
- **Use The In-Built Troubleshooter**: run "python troubleshoot.py" for enviroment validation , dependencies , and cog setup
- **Fix Common Setup Issues**:run "python fix.py" to fix common issuse at setup
## License

Use this template freely and customize it however you like.

# Useful links
- https://www.youtube.com/watch?v=CHbN_gB30Tw&list=PL-7Dfw57ZZVQ-GCNQS4Kyz637Fffhb0Hs&index=1
- https://www.youtube.com/watch?v=YD_N6Ffoojw
