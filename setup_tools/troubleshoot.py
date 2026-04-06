"""Troubleshoot common bot setup issues.

Run this script to verify your Python environment, required packages, token, and cog files.
"""

import importlib
import os
import sys

from dotenv import load_dotenv


def check_python_version():
    print(f"Python version: {sys.version.split()[0]}")
    if sys.version_info < (3, 8):
        print("[!] Python 3.8 or higher is required.")


def load_environment():
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        load_dotenv(env_path)
        print("[+] Loaded .env file.")
    else:
        print("[!] .env file not found. Create one with DISCORD_TOKEN=your_token_here")

    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("[!] DISCORD_TOKEN is not set.")
    else:
        print("[+] DISCORD_TOKEN is set.")

    return token


def check_dependencies():
    missing = []
    for module_name in ["discord", "dotenv"]:
        try:
            importlib.import_module(module_name)
            print(f"[+] {module_name} is installed.")
        except ImportError:
            missing.append(module_name)
            print(f"[!] {module_name} is missing.")

    if missing:
        print("[+] Install missing packages with: pip install " + " ".join(missing))


def check_project_structure():
    print("\nChecking project files...")
    required = ["main.py", "config.py", "core/bot.py", "core/events.py", "core/errors.py"]
    for path in required:
        if os.path.exists(path):
            print(f"[+] {path}")
        else:
            print(f"[!] {path} is missing.")

    if os.path.isdir("cogs"):
        cog_files = [f for f in os.listdir("cogs") if f.endswith(".py")]
        print(f"[+] Found {len(cog_files)} cog file(s): {', '.join(cog_files) if cog_files else 'none'}")
    else:
        print("[!] cogs/ directory is missing.")


def try_imports():
    print("\nTesting imports...")
    try:
        from config import TOKEN
        print("[+] Imported config.TOKEN.")
    except Exception as exc:
        print(f"[!] Failed to import config.TOKEN: {exc}")

    try:
        from core.bot import create_bot
        bot = create_bot()
        print("[+] create_bot() works.")
    except Exception as exc:
        print(f"[!] Failed to create bot instance: {exc}")


if __name__ == "__main__":
    print("Discord Bot Troubleshooter")
    print("===========================\n")
    check_python_version()
    check_dependencies()
    token = load_environment()
    check_project_structure()
    try_imports()
    if token:
        print("\nIf all checks passed, try running: python main.py")
