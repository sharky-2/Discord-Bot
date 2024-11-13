import asyncio
from Api.Project.Server import setting
from Api.Project.Server.Utility import bot_utilitys

# -----------------------------------------------------------------------------------------------------------
# Position of text
async def position_command(message, has_role):
    botCommands = bot_utilitys.moderator_commands.get(message.content, False)
    if message.content.lower().startswith("$pos"): 
        if botCommands:
            if has_role("🟠OWNER") or has_role("🔵ADMIN"):
                bot_message = await message.channel.send(
                    f"📍 COMMAND: \t`{message.content}` \n"
                    f"📝 AUTHOR: \t`{message.author}` \n"
                    f"📺 CHANNEL: \t`{message.channel.name}`"
                )
                if setting.settings.get("delete_commands_messages", False):
                    await asyncio.sleep(10)
                    try: await message.delete(); await bot_message.delete()
                    except: pass
            else: 
                bot_message = await message.channel.send(
                    "❌ You can't use this command. You lack the necessary permissions!"
                )
                if setting.settings.get("delete_commands_messages", False):
                    await asyncio.sleep(10)
                    try: await message.delete(); await bot_message.delete()
                    except: pass
        else: 
            bot_message = await message.channel.send(
                f"**❌ Command Disabled**\n"
                f"The command `{message.content}` is currently turned **OFF**."
                f"Try again later."
            )
            if setting.settings.get("delete_commands_messages", False):
                await asyncio.sleep(10)
                try: await message.delete(); await bot_message.delete()
                except: pass

# -----------------------------------------------------------------------------------------------------------
# Clear chat
async def clear_command(message, has_role):
    botCommands = bot_utilitys.moderator_commands.get(message.content, False)
    if message.content.lower().startswith("$clear"): 
        if botCommands:
            # Check if user has role Owner or Admin
            if has_role("🟠OWNER") or has_role("🔵ADMIN"):
                await message.delete()
                deleted = await message.channel.purge(limit=500) 
                confirmation_message = await message.channel.send(
                    f"🗑️ Deleted `{len(deleted)}` messages.", delete_after=5
                )
            else:
                bot_message = await message.channel.send(
                    "❌ You can't use this command. You lack the necessary permissions!"
                )
                if setting.settings.get("delete_commands_messages", False): 
                    await asyncio.sleep(5)
                    await message.delete()
                    await bot_message.delete()
        else:
            bot_message = await message.channel.send(
                f"**❌ Command Disabled**\n"
                f"The command `{message.content}` is currently turned **OFF**."
            )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
