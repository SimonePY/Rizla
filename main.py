import disnake
import tomlkit
from disnake.ext import commands
from collections import defaultdict
from pathlib import Path
from typing import Dict

CONFIG_FILE: Path = Path("config.toml")

if not CONFIG_FILE.exists():
    CONFIG_FILE.touch()
    CONFIG_FILE.write_text(
        'bot_token: str = "" #You have to put your own bot token here. \n\n\napi_key: str = "" #You have to put your own api key here.'
    )

config: Dict[str, str] = defaultdict(str, tomlkit.loads(CONFIG_FILE.read_text()))

bot: commands.Bot = commands.Bot(
    command_prefix="%",
    activity=disnake.Activity(name="Use /about", type=disnake.ActivityType.playing),
    intents=disnake.Intents.all(),
    help_command=None,
)

try:
    bot.run(config["api_key"])
except disnake.LoginFailure:
    print("The provided bot token is invalid.")
except tomlkit.toml.TOMLDecodeError:
    print("The configuration file is not properly formatted.")
except KeyError as e:
    print(f"The configuration file is missing the key '{str(e)}'.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
