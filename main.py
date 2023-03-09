import disnake
import tomlkit
import databaseHandler
from disnake.ext import commands
from collections import defaultdict
from pathlib import Path
from typing import Dict

CONFIG_FILE: Path = Path("config.toml")

if not CONFIG_FILE.exists():
    CONFIG_FILE.touch()
    CONFIG_FILE.write_text(
        "discord_bot_token = ''\npwn_api_key = ''\ndiscord_bot_activity = ''\ndiscord_bot_case =\ndiscord_bot_prefix = ''\ndiscord_bot_description = ''\ndiscord_bot_owner = ''\ndiscord_bot_reload =\ndiscord_bot_status = ''\ndiscord_bot_strip =\ndiscord_sync_debug =\n"
    )
config: Dict[str, str] = defaultdict(str, tomlkit.loads(CONFIG_FILE.read_text()))

bot: commands.Bot = commands.Bot(
    activity=disnake.Activity(
        name=config.get("discord_bot_activity", ""), type=disnake.ActivityType.playing
    ),
    case_insensitive=config.get("discord_bot_sensitive"),
    command_prefix=config.get("discord_bot_prefix"),
    description=config.get("discord_bot_description"),
    owner_id=config.get("discord_bot_owner_id"),
    reload=config.get("discord_bot_reload"),
    status=config.get("discord_bot_status", ""),
    strip_after_prefix=config.get("discord_bot_strip"),
    sync_commands_debug=config.get("discord_sync_debug"),
    help_command=None,
    intents=disnake.Intents.all(),
)

if __name__ == "__main__":
    try:
        databaseHandler
        bot.run(config.get("discord_bot_token"))
    except disnake.LoginFailure as e:
        print(f"The provided bot token is invalid, exception: '{str(e)}'")
    except tomlkit.toml.TOMLDecodeError as e:
        print(
            f"The configuration file is not properly formatted, exception: '{str(e)}'"
        )
    except KeyError as e:
        print(f"The configuration file is missing the key exception: '{str(e)}'")
    except Exception as e:
        print(f"An unexpected error occurred:'{str(e)}'")
