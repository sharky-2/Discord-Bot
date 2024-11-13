import asyncio
from Api.Project.Server import setting
from Api.Project.Server.Utility import bot_utilitys
from Api.Project.Server.other import channel_responses

# -----------------------------------------------------------------------------------------------------------
# Info command
async def info_command(message):
    botCommands = bot_utilitys.general_commands.get(message.content, False)
    if message.content.startswith("$info"):
        if botCommands: 
            text = ""
            for char in channel_responses.keys():
                if message.channel.name[1:] == char: 
                    text += channel_responses[char]
            bot_message = await message.channel.send(text)
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete() 
        else: 
            bot_message = await message.channel.send(
                f"**❌ Command Disabled\n**\n"
                f"The command `{message.content}` is currently turned **OFF**."
                f"Try again later."
            )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()

# -----------------------------------------------------------------------------------------------------------
# BotInfo
async def botinfo_command(message):
    botCommands = bot_utilitys.general_commands.get(message.content, False)
    if message.content.lower().startswith("$botinfo"):
        if botCommands:
            text = (
                f"👋 Hello {message.author.mention}, I'm your school project bot! "
                "My role in this server is to assist and control various tasks. "
                "If you need help, just call me using `$help`."
            )
            bot_message = await message.channel.send(text)
            if setting.settings.get("delete_commands_messages", False): 
                await asyncio.sleep(15); await message.delete(); await bot_message.delete()
        else: 
            bot_message = await message.channel.send(
                f"**❌ Command Disabled\n**\n"
                f"The command `{message.content}` is currently turned **OFF**."
                f"Try again later."
            )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()

# -----------------------------------------------------------------------------------------------------------
# Invite
async def invite_command(message):
    botCommands = bot_utilitys.general_commands.get(message.content, False)
    if message.content.lower().startswith("$invite"):
        if botCommands:
            bot_message = await message.channel.send("🔗 Here is the invite link: `https://discord.gg/C5cAPrcd`")
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(8); await message.delete(); await bot_message.delete()
        else: 
            bot_message = await message.channel.send(
                    f"**❌ Command Disabled\n**\n"
                    f"The command `{message.content}` is currently turned **OFF**."
                    f"Try again later."
                )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()

# -----------------------------------------------------------------------------------------------------------
# User info
async def userInfo_command(message):
    com = message.content.lower().split()[0]
    botCommands = bot_utilitys.general_commands.get(message.content.split()[0], False)

    if message.content.lower().startswith("$userinfo"):
        parts = message.content.split()
        if len(parts) > 1: 
            com_user = parts[1]
            member = message.guild.get_member_named(com_user)

            if member is not None:
                roles = [role.name for role in member.roles if role.name != "@everyone"]

                if botCommands:
                    roles = [role.name for role in message.author.roles if role.name != "@everyone"]
                    role_count = len(roles)

                    roles_list = ', '.join(roles) if roles else "No roles"
                    response_message = f"👤 User: `{com_user}`\n📜 Roles: `({role_count}): {roles_list}`"
                    bot_message = await message.channel.send(response_message)
                    if setting.settings.get("delete_commands_messages", False): 
                        await asyncio.sleep(8); await message.delete(); await bot_message.delete()

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
                    f"**❌ Member Errore\n**\n"
                    f"Member that you tried to call doesn't exist in this server."
                    f"Try again later or put another Member name."
                )
                if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
        else:
            bot_message = await message.channel.send(
                    f"**📝 Missing Member Query\n**\n"
                    f"You forgot to add Member name\n"         
                    f"Try using: `{com} <member>`\n"
                    "Example: `$userinfo pfyber`"
                )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()

# -----------------------------------------------------------------------------------------------------------
# Rank
async def rank_command(message):
    com = message.content.lower().split()[0]
    botCommands = bot_utilitys.general_commands.get(message.content, False)

    if message.content.lower().startswith("$rank"):
        if botCommands:
            roles = [role.name for role in message.author.roles if role.name != "@everyone"]
            role_count = len(roles)
            roles_list = ', '.join(roles) if roles else "No roles"
            response_message = f"👤 User: `{message.author}`\n📜 Roles `({role_count}): {roles_list}`"
            bot_message = await message.channel.send(response_message)

            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(8); await message.delete(); await bot_message.delete()
        else: 
            bot_message = await message.channel.send(
                f"**❌ Command Disabled\n**"
                f"The command `{com}` is currently turned **OFF**."
                f"Try again later."
            )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()

# -----------------------------------------------------------------------------------------------------------
# Commands
async def commands(message):
    com = message.content.lower().split()[0]
    botCommands = bot_utilitys.general_commands.get(message.content, False)
    
    # -----------------------------------------------------------------------------------------------------------
    if message.content.lower().startswith("$commands"):
        if botCommands:

            # Channels
            general_channel = ["chat", "pics", "videos", "music", "games", "meme"]
            browser_channel = ["browser"]
            games_channel = ["math", "guess", "other"]
            bot_channel = ["commands"]
            
            # -----------------------------------------------------------------------------------------------------------
            # General Channel Commands
            if any(char in message.channel.name for char in general_channel):
                bot_message = await message.channel.send(

                    f"**⚪ General Commands**\n"
                    f"`{'✅' if bot_utilitys.general_commands['$help'] else '❌'}$help`: Move you to info channel\n"
                    f"`{'✅' if bot_utilitys.general_commands['$info'] else '❌'}$info`: Tell about channel that you are at\n"
                    f"`{'✅' if bot_utilitys.general_commands['$invite'] else '❌'}$invite`: Invite others to the group\n"
                    f"`{'✅' if bot_utilitys.general_commands['$userinfo'] else '❌'}$userinfo`: Provides user information (roles, name)\n"
                    f"`{'✅' if bot_utilitys.general_commands['$rank'] else '❌'}$rank`: Displays your ranks in this server\n"
                    f"`{'✅' if bot_utilitys.general_commands['$commands'] else '❌'}$commands`: Show all commands for that channel\n\n"

                    f"`{'✅' if bot_utilitys.meme_commands['$joke'] else '❌'}$joke`: Bot will tell you random jokes\n"
                    f"`{'✅' if bot_utilitys.meme_commands['$randomfact'] else '❌'}$randomfact`: Bot will give you a random fact\n\n"

                    f"**🟠 Moderator Commands**\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$pos'] else '❌'}$pos`: Show stats of this channel\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$ban'] else '❌'}$ban`: Ban a user from the server\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$kick'] else '❌'}$kick`: Kick a user from the server\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$warn'] else '❌'}$warn`: Warn a user, typically for bad behavior\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$clear'] else '❌'}$clear`: Clear text in channel\n\n"

                )

                bot_message2 = await message.channel.send(
                    f"`❌ Command is disabled \t|\t"
                    f"✅ Command is enabled`"
                )  

                if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(20); await message.delete(); await bot_message.delete(); await bot_message2.delete()

            # -----------------------------------------------------------------------------------------------------------
            # Browser Channel Commands
            if any(char in message.channel.name for char in browser_channel):
                bot_message = await message.channel.send(

                    f"**⚪ General Commands**\n"
                    f"`{'✅' if bot_utilitys.general_commands['$help'] else '❌'}$help`: Move you to info channel\n"
                    f"`{'✅' if bot_utilitys.general_commands['$info'] else '❌'}$info`: Tell about channel that you are at\n"
                    f"`{'✅' if bot_utilitys.general_commands['$commands'] else '❌'}$commands`: Show all commands for that channel\n\n"

                    f"**🟠 Moderator Commands**\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$pos'] else '❌'}$pos`: Show stats of this channel\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$ban'] else '❌'}$ban`: Ban a user from the server\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$kick'] else '❌'}$kick`: Kick a user from the server\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$warn'] else '❌'}$warn`: Warn a user, typically for bad behavior\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$clear'] else '❌'}$clear`: Clear text in channel\n\n"

                    f"**🔴 Browser Commands**\n"
                    f"`{'✅' if bot_utilitys.browsers['$wiki'] else '❌'}$wiki`: No description\n"
                    f"`{'✅' if bot_utilitys.browsers['$youtube'] else '❌'}$youtube`: No description\n"
                    f"`{'✅' if bot_utilitys.browsers['$google'] else '❌'}$google`: No description\n\n"

                )

                bot_message2 = await message.channel.send(
                    f"`❌ Command is disabled \t|\t"
                    f"✅ Command is enabled`"
                )   

                if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(20); await message.delete(); await bot_message.delete(); await bot_message2.delete()
            
            # -----------------------------------------------------------------------------------------------------------
            # Game Channel Commands
            if any(char in message.channel.name for char in games_channel):
                bot_message = await message.channel.send(

                    f"**⚪ General Commands**\n"
                    f"`{'✅' if bot_utilitys.general_commands['$help'] else '❌'}$help`: Move you to info channel\n"
                    f"`{'✅' if bot_utilitys.general_commands['$info'] else '❌'}$info`: Tell about channel that you are at\n"
                    f"`{'✅' if bot_utilitys.general_commands['$commands'] else '❌'}$commands`: Show all commands for that channel\n\n"

                    f"`{'✅' if bot_utilitys.meme_commands['$joke'] else '❌'}$joke`: Bot will tell you random jokes\n"
                    f"`{'✅' if bot_utilitys.meme_commands['$randomfact'] else '❌'}$randomfact`: Bot will give you a random fact\n\n"

                    f"**🟠 Moderator Commands**\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$pos'] else '❌'}$pos`: Show stats of this channel\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$ban'] else '❌'}$ban`: Ban a user from the server\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$kick'] else '❌'}$kick`: Kick a user from the server\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$warn'] else '❌'}$warn`: Warn a user, typically for bad behavior\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$clear'] else '❌'}$clear`: Clear text in channel\n\n"

                    f"**🟡 Game Commands**\n"
                    f"`{'✅' if bot_utilitys.game_commands['$math'] else '❌'}$math`: Math exercises :D\n"
                    f"`{'✅' if bot_utilitys.game_commands['$word'] else '❌'}$word`: A random word will be chosen and users will have to guess it\n"
                    f"`{'✅' if bot_utilitys.game_commands['$game steam'] else '❌'}$game steam`: Random game available on Steam\n"
                    f"`{'✅' if bot_utilitys.game_commands['$game epic'] else '❌'}$game epic`: Random game available on Epic Games\n"
                    f"`{'✅' if bot_utilitys.game_commands['$game browser'] else '❌'}$game browser`: Random game available on Browser\n\n"

                )

                bot_message2 = await message.channel.send(
                    f"`❌ Command is disabled \t|\t"
                    f"✅ Command is enabled`"
                )  

                if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(20); await message.delete(); await bot_message.delete(); await bot_message2.delete()
            
            # -----------------------------------------------------------------------------------------------------------
            # Bots Channel Commands
            if any(char in message.channel.name for char in bot_channel):
                bot_message = await message.channel.send(

                    f"**⚪ General Commands**\n"
                    f"`{'✅' if bot_utilitys.general_commands['$help'] else '❌'}$help`: Move you to info channel\n"
                    f"`{'✅' if bot_utilitys.general_commands['$info'] else '❌'}$info`: Tell about channel that you are at\n"
                    f"`{'✅' if bot_utilitys.general_commands['$botinfo'] else '❌'}$botinfo`: Tells about bot\n"
                    f"`{'✅' if bot_utilitys.general_commands['$invite'] else '❌'}$invite`: Invite others to the group\n"
                    f"`{'✅' if bot_utilitys.general_commands['$userinfo'] else '❌'}$userinfo`: Provides user information (roles, name)\n"
                    f"`{'✅' if bot_utilitys.general_commands['$rank'] else '❌'}$rank`: Displays your ranks in this server\n"
                    f"`{'✅' if bot_utilitys.general_commands['$commands'] else '❌'}$commands`: Show all commands for that channel\n\n"
                    
                    f"**🟠 Moderator Commands**\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$pos'] else '❌'}$pos`: Show stats of this channel\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$ban'] else '❌'}$ban`: Ban a user from the server\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$kick'] else '❌'}$kick`: Kick a user from the server\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$warn'] else '❌'}$warn`: Warn a user, typically for bad behavior\n"
                    f"`{'✅' if bot_utilitys.moderator_commands['$clear'] else '❌'}$clear`: Clear text in channel\n\n"

                )

                bot_message2 = await message.channel.send(
                    f"`❌ Command is disabled \t|\t"
                    f"✅ Command is enabled`"
                )  

                if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(20); await message.delete(); await bot_message.delete(); await bot_message2.delete()
        else:
            bot_message = await message.channel.send(
                f"**❌ Command Disabled\n**\n"
                f"The command `{com}` is currently turned **OFF**. "
                f"Try again later."
            )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()
            return
