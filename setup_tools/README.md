# Setup Tools

This folder contains helper scripts to make getting your bot running easier.

## fix.py

- Creates a `.env` file if one is missing.
- Creates the `cogs/` directory if it does not exist.
- Installs missing dependencies (`discord.py`, `python-dotenv`).

Run it with:

```bash
python setup_tools/fix.py
```

## troubleshoot.py

- Verifies your Python version.
- Checks for required packages.
- Confirms `.env` and `cogs/` exist.
- Tests importing `config` and creating the bot.

Run it with:

```bash
python setup_tools/troubleshoot.py
```
