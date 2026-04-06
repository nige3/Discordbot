"""Fix common Discord bot setup issues.

Run this script to generate a default .env file, install missing dependencies,
and make sure the `cogs/` folder exists.
"""

import os
import subprocess
import sys


def ensure_env_file():
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        print("[+] .env file already exists.")
        return

    print("[+] Creating a new .env file with placeholder values...")
    with open(env_path, "w", encoding="utf-8") as env_file:
        env_file.write("DISCORD_TOKEN=your_bot_token_here\n")
    print("[+] Created .env. Edit it with your Discord bot token.")


def ensure_cogs_folder():
    cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
    if os.path.isdir(cogs_dir):
        print("[+] cogs/ directory exists.")
        return

    print("[+] Creating cogs/ directory...")
    os.makedirs(cogs_dir, exist_ok=True)
    print("[+] Created cogs/ directory. Add your cog files here.")


def install_dependencies():
    required = ["discord.py", "python-dotenv"]
    missing = []
    for package in required:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            missing.append(package)

    if not missing:
        print("[+] All required dependencies are installed.")
        return

    print("[+] Installing missing dependencies: {}".format(", ".join(missing)))
    subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
    print("[+] Dependencies installed.")


def main():
    print("[+] Fixing common Discord bot setup issues...")
    ensure_env_file()
    ensure_cogs_folder()
    install_dependencies()
    print("\nAll done! Review the .env file and run `python main.py`.")


if __name__ == "__main__":
    main()
