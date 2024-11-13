import random as rng
import asyncio
import discord
from discord import Embed
from Api.Project.Server import setting
from Api.Project.Server.Utility import bot_utilitys
from Api.Project.Server.General_channel import jokes

# -----------------------------------------------------------------------------------------------------------
# Random joke
async def randomJoke(message):
    com = message.content.lower().split()[0]
    botCommands = bot_utilitys.meme_commands.get(message.content.lower(), False)
    if message.content.lower().startswith("$joke") and message.content != "$clear":
        if botCommands:
            if "meme" in message.channel.name:
                embed = Embed(
                    title = f"**😂 Random joke** `{len(jokes.funny_jokes)} jokes found`",
                    description = f"{rng.choice(jokes.funny_jokes)}",
                    color = discord.Color.blue()
                )
                await message.channel.send(embed=embed)
                    
            else:
                bot_message = await message.channel.send(
                    f"**⚠️ Wrong Channel\n**\n"
                    f"To use `{message.content}`, please go to the **#😂meme** channel."
                )
                if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()

        else:
            bot_message = await message.channel.send(
                    f"**❌ Command Disabled\n**"
                    f"The command `{com}` is currently turned **OFF**."
                    f"Try again later."
                )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete() 