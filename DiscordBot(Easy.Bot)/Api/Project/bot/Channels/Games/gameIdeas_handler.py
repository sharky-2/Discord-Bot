import asyncio
import discord
from discord import Embed
import random as rng
from Api.Project.Server.Utility import bot_utilitys
from Api.Project.Server import setting
from Api.Project.Server.Game_channel import game_ideas

# -----------------------------------------------------------------------------------------------------------
# Give Game
# -----------------------------------------------------------------------------------------------------------
async def game(message):
    botCommands = bot_utilitys.game_commands.get(message.content.lower(), False)
    com = message.content.lower().split()[0]

    # -----------------------------------------------------------------------------------------------------------
    # Steam
    if message.content.lower().startswith("$game steam"):
        if "other" in message.channel.name:
            if botCommands:
                game_title = rng.choice(game_ideas.steam_game_ideas)
                embed = Embed(
                    title="🎮 Steam Game",
                    description=f"Random pick: **{game_title}**",
                    color = discord.Color.green()
                )
                embed.set_footer(text=f"{len(game_ideas.steam_game_ideas)} games found")
                bot_message = await message.channel.send(embed=embed)

                # Delete Messages
                if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(20); await message.delete(); await bot_message.delete()
            else:
                bot_message = await message.channel.send(
                    f"**❌ Command Disabled\n**\n"
                    f"The command `{message.content}` is currently turned **OFF**."
                    f"Try again later."
                )
                if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
        else:
            bot_message = await message.channel.send(
                f"**⚠️ Wrong Channel\n**\n"
                f"To use `{message.content}`, please go to the **#🧩other** channel."
            )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
    
    # -----------------------------------------------------------------------------------------------------------
    # Epic Games
    elif message.content.lower().startswith("$game epic"):
        if "other" in message.channel.name:
            if botCommands:
                game_title = rng.choice(game_ideas.epic_games_ideas)
                embed = Embed(
                    title = "🎮 Epic Games Game",
                    description = f"Random pick: **{game_title}**",
                    color = discord.Color.red()
                )
                embed.set_footer(text=f"{len(game_ideas.steam_game_ideas)} games found")
                bot_message = await message.channel.send(embed=embed)

                # Delete Messages
                if setting.settings.get("delete_commands_messages", False): 
                    await asyncio.sleep(20); await message.delete(); await bot_message.delete()
            else:
                bot_message = await message.channel.send(
                    f"**❌ Command Disabled\n**\n"
                    f"The command `{message.content}` is currently turned **OFF**."
                    f"Try again later."
                )
                if setting.settings.get("delete_commands_messages", False): 
                    await asyncio.sleep(5); await message.delete(); await bot_message.delete()
        else:
            bot_message = await message.channel.send(
                f"**⚠️ Wrong Channel\n**\n"
                f"To use `{message.content}`, please go to the **#🧩other** channel."
            )
            if setting.settings.get("delete_commands_messages", False): 
                await asyncio.sleep(5); await message.delete(); await bot_message.delete()
    
    # -----------------------------------------------------------------------------------------------------------
    # Browser
    elif message.content.lower().startswith("$game browser"):
        if "other" in message.channel.name:
            if botCommands:
                game_title = rng.choice(game_ideas.browser_game_ideas)
                embed = Embed(
                    title="🎮 Browser Game",
                    description = f"Random pick: **{game_title}**",
                    color = discord.Color.blue()
                )
                embed.set_footer(text=f"{len(game_ideas.steam_game_ideas)} games found")
                bot_message = await message.channel.send(embed=embed)

                # Delete Messages
                if setting.settings.get("delete_commands_messages", False): 
                    await asyncio.sleep(20); await message.delete(); await bot_message.delete()
            else:
                bot_message = await message.channel.send(
                    f"**❌ Command Disabled\n**\n"
                    f"The command `{message.content}` is currently turned **OFF**."
                    f"Try again later."
                )
                if setting.settings.get("delete_commands_messages", False): 
                    await asyncio.sleep(5); await message.delete(); await bot_message.delete()
            
        else:
            bot_message = await message.channel.send(
                f"**⚠️ Wrong Channel**\n"
                f"To use `{message.content}`, please go to the **#🧩other** channel."
            )
            if setting.settings.get("delete_commands_messages", False): 
                await asyncio.sleep(5); await message.delete(); await bot_message.delete()
    
    # -----------------------------------------------------------------------------------------------------------
    # Command Formatting Errore
    elif message.content.lower().startswith("$game"): 
        if "other" in message.channel.name:
            # Message
            bot_message = await message.channel.send(
                f"**📝 Missing Search Query\n**\n"
                f"You forgot to specify where you want to play game\n"
                f"Try using: `{com} <steam, epic, browser>`\n"
                "Example: `$game steam`"
            )

            # Delete Messages
            if setting.settings.get("delete_commands_messages", False): 
                await asyncio.sleep(20); await message.delete(); await bot_message.delete()
            
        else:
            # MEssage
            bot_message = await message.channel.send(
                f"**⚠️ Wrong Channel**\n"
                f"To use `{message.content}`, please go to the **#🧩other** channel."
            )

            # Delete Message
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()