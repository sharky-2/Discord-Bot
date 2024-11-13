import random as rng
import asyncio
from Api.Project.Server.Utility import bot_utilitys
from Api.Project.Server import setting

# -----------------------------------------------------------------------------------------------------------
# Math games
async def math(message):
    com = message.content.lower().split()[0]

    # Check command
    botCommands = bot_utilitys.game_commands.get(message.content.lower(), False)
    if message.content.lower().startswith("$math") and message.content != "$clear":
        if "math" in message.channel.name:
            if botCommands:

                # Random values
                if "math" in message.channel.name:
                    await message.channel.send("**🔢 Random Math Exercise**")
                    await message.channel.send("`Addition (+) | Subtraction (-) | Multiplication (*) | Division (/)`")

                    for i in range(25):
                        n1 = rng.randint(0, 1000)
                        n2 = rng.randint(1, 1000)  

                        await message.channel.send(
                            f"**Question {i + 1}:**\n"
                            f"{n1} + {n2} = `?`\n"
                            f"{n1} - {n2} = `?`\n"
                            f"{n1} * {n2} = `?`\n"
                            f"{n1} / {n2} = `?`"
                        )
                        await asyncio.sleep(5)
            
            else:
                bot_message = await message.channel.send(
                    f"**❌ Command Disabled\n**"
                    f"The command `{com}` is currently turned **OFF**."
                    f"Try again later."
                )
                if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete() 
        else:
            bot_message = await message.channel.send(
                f"**⚠️ Wrong Channel\n**\n"
                f"To use `{message.content}`, please go to the **#🔢math** channel."
            )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
 
