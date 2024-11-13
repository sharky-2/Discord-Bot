import asyncio
import discord
from discord import Embed
from Api.Project.Server import setting
from Api.Project.Server.Utility import bot_utilitys

# -----------------------------------------------------------------------------------------------------------
# Wiki Browser
# -----------------------------------------------------------------------------------------------------------
async def wiki_browser(message):
    com = message.content.lower().split()[0]
    browserCommands = bot_utilitys.browsers.get(com, False)
    
    # -----------------------------------------------------------------------------------------------------------
    # Wiki - Wikipedia
    if message.content.lower().startswith("$wiki"):
        if "⌨" in message.channel.name: 
            if browserCommands:
                parts = message.content.split()
                if len(parts) > 1: 
                    com_user = parts[1]

                    # -----------------------------------------------------------------------------------------------------------
                    # Check if user called command right
                    if len(parts) > 2 and "-" not in parts:
                        # Message
                        bot_message = await message.channel.send(
                            "**❌ Command Formatting Error\n**"
                            f"Oops! It looks like you missed a dash (`-`) between parts of your command.\n"         
                            f"Your command: `{message.content.lower()}`\n"
                            f"Correct format: `{com} {parts[1]}-{parts[2]}...`\n"
                            "Example: `$wiki history-of-python`"
                        )

                        # Delete Messages
                        if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(10); await message.delete(); await bot_message.delete()

                    elif "⌨" in message.channel.name:
                        # Message
                        embed = Embed(
                            title = f"📺 Wiki Search: {com_user}",
                            description = f"https://www.wikipedia.org/wiki/{com_user}",
                            color = discord.Color.light_gray()
                        )
                        bot_message = await message.channel.send(embed=embed)

                        # Delete Message
                        if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(20); await message.delete(); await bot_message.delete()

                else:
                    # Message
                    bot_message = await message.channel.send(
                        "**📝 Missing Search Query\n**"
                        f"You forgot to specify what you're looking for on Wikipedia\n"         
                        f"Try using: `{com} <topic>`\n"
                        "Example: `$wiki history-of-python`"
                    )

                    # Delete Message
                    if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
            else:
                # Message
                bot_message = await message.channel.send(
                    f"**❌ Command Disabled\n**"
                    f"The command `{com}` is currently turned **OFF**."
                    f"Try again later."
                )

                # Delete Message
                if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
        else:
            bot_message = await message.channel.send(
                f"**⚠️ Wrong Channel\n**\n"
                f"To use `{message.content}`, please go to the **#⌨bot-browser** channel."
            )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()

# -----------------------------------------------------------------------------------------------------------
# YouTube Browser
# -----------------------------------------------------------------------------------------------------------
async def youtube_browser(message):
    com = message.content.lower().split()[0]
    browserCommands = bot_utilitys.browsers.get(com, False)
    
    # -----------------------------------------------------------------------------------------------------------
    # YouTube Search
    if message.content.lower().startswith("$youtube"):
        if "⌨" in message.channel.name: 
            if browserCommands:
                parts = message.content.split()
                if len(parts) > 1:
                    com_user = parts[1]

                    # Check if user called command right
                    if len(parts) > 2 and "-" not in parts:
                        # Message
                        bot_message = await message.channel.send(
                            "**❌ Command Formatting Error\n**"
                            f"Oops! It looks like you missed a dash (`-`) between parts of your command.\n"
                            f"Your command: `{message.content.lower()}`\n"
                            f"Correct format: `{com} {parts[1]}-{parts[2]}...`\n"
                            "Example: `$youtube learn-python-basics`"
                        )

                        # Delete Messages
                        if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(10); await message.delete(); await bot_message.delete()

                    else:
                        embed = Embed(
                            title = f"📺 Youtube Search: {com_user}",
                            description = f"https://www.youtube.com/results?search_query={com_user}",
                            color = discord.Color.red()
                        )
                        bot_message = await message.channel.send(embed=embed)

                        # Delete Message
                        if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(20); await message.delete(); await bot_message.delete()

                else:
                    # Message
                    bot_message = await message.channel.send(
                        "**📝 Missing Search Query\n**"
                        f"You forgot to specify what you're trying to find on YouTube\n"
                        f"Try using: `{com} <topic>`\n"
                        "Example: `$youtube learn-python-basics`"
                    )

                    # Delete Message
                    if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
            else:
                # Message
                bot_message = await message.channel.send(
                    f"**❌ Command Disabled\n**"
                    f"The command `{com}` is currently turned **OFF**."
                    f"Try again later."
                )

                # Delete Message
                if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
        else:
            bot_message = await message.channel.send(
                f"**⚠️ Wrong Channel\n**\n"
                f"To use `{message.content}`, please go to the **#⌨bot-browser** channel."
            )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()

# -----------------------------------------------------------------------------------------------------------
# Google Browser
# -----------------------------------------------------------------------------------------------------------
async def youtube_browser(message):
    com = message.content.lower().split()[0]
    browserCommands = bot_utilitys.browsers.get(com, False)
    
    # -----------------------------------------------------------------------------------------------------------
    # Google Search
    if message.content.lower().startswith("$google"):
        if "⌨" in message.channel.name: 
            if browserCommands:
                parts = message.content.split()
                if len(parts) > 1:
                    com_user = parts[1]

                    # Check if user called command right
                    if len(parts) > 2 and "-" not in parts:
                        # Message
                        bot_message = await message.channel.send(
                            "**❌ Command Formatting Error\n**"
                            f"Oops! It looks like you missed a dash (`-`) between parts of your command.\n"
                            f"Your command: `{message.content.lower()}`\n"
                            f"Correct format: `{com} {parts[1]}-{parts[2]}...`\n"
                            "Example: `$google learn-python-basics`"
                        )

                        # Delete Messages
                        if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(10); await message.delete(); await bot_message.delete()

                    else:
                        embed = Embed(
                            title = f"📺 Google Search: {com_user}",
                            description = f"https://www.google.com/search?q={com_user}",
                            color = discord.Color.red()
                        )
                        bot_message = await message.channel.send(embed=embed)

                        # Delete Message
                        if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(20); await message.delete(); await bot_message.delete()

                else:
                    # Message
                    bot_message = await message.channel.send(
                        "**📝 Missing Search Query\n**"
                        f"You forgot to specify what you're trying to find on YouTube\n"
                        f"Try using: `{com} <topic>`\n"
                        "Example: `$google learn-python-basics`"
                    )

                    # Delete Message
                    if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
            else:
                # Message
                bot_message = await message.channel.send(
                    f"**❌ Command Disabled\n**"
                    f"The command `{com}` is currently turned **OFF**."
                    f"Try again later."
                )

                # Delete Message
                if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
        else:
            bot_message = await message.channel.send(
                f"**⚠️ Wrong Channel\n**\n"
                f"To use `{message.content}`, please go to the **#⌨bot-browser** channel."
            )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
