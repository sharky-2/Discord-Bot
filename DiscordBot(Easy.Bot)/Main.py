# -----------------------------------------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------------------------------------
import discord
import os
from discord.ext import commands

# -----------------------------------------------------------------------------------------------------------
# CALL FILES
# -----------------------------------------------------------------------------------------------------------
# API KEY
from Api.Config.api_key import API_KEY

# ADMIN FOLDER
from Api.Project.bot.Admin.admin_handler import kick

# CHANNEL FOLDER
from Api.Project.bot.Channels import link_handler
from Api.Project.bot.Channels.General import random_joke

from Api.Project.bot.Channels.Games import gameIdeas_handler
from Api.Project.bot.Channels.Games import math_handler
from Api.Project.bot.Channels.Games import guessWord_handler

from Api.Project.bot.Channels.Browser import browser_handler

# COMMANDS FOLDER
from Api.Project.bot.commands import expression_handler
from Api.Project.bot.commands import general_commands
from Api.Project.bot.commands import admin_commands

# SERVER COMMANDS -> TRUE / FALSE
from Api.Project.Server import setting
from Api.Project.Server.Utility import bot_utilitys

# TEST
from Api.Project.test.testComand import test

# -----------------------------------------------------------------------------------------------------------
def clear(): os.system("cls")
def bot():
    # ----------------------------------------------------------------------------------------------------------- 
    # BOT
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True                                                                                                                       
    bot = commands.Bot(command_prefix = "$", intents = intents)

    # -----------------------------------------------------------------------------------------------------------
    # START EASY.BOT
    @bot.event
    async def on_ready(): 
        print(f"\nWE HAVE LOGGED IN AS [{bot.user}]") 
        await print_all_users_roles()
        #await check_utilitys()

    # -----------------------------------------------------------------------------------------------------------
    @bot.event
    async def on_message(message):
        if message.author == bot.user: return 
        # -----------------------------------------------------------------------------------------------------------
        # CHECK USERS ROLES
        role_names = [role.name for role in message.author.roles]
        def has_role(role_name): return role_name in role_names

        # -----------------------------------------------------------------------------------------------------------
        # TEST
        await test(message)

        # -----------------------------------------------------------------------------------------------------------
        # EXPRESSION HANDLER
        await expression_handler.handle_greetings(message)
        await expression_handler.handle_farewells(message)

        # -----------------------------------------------------------------------------------------------------------
        # CHANNEL HANDLER
        await link_handler.handle_links(message)
        await browser_handler.wiki_browser(message)
        await browser_handler.youtube_browser(message)
        await gameIdeas_handler.game(message)
        await math_handler.math(message)
        await guessWord_handler.guessWord(message)
        await guessWord_handler.randomWord(message)
        await random_joke.randomJoke(message)

        # -----------------------------------------------------------------------------------------------------------
        # GENERAL / EVERY ONE COMMANDS
        await general_commands.info_command(message)
        await general_commands.botinfo_command(message)
        await general_commands.invite_command(message)
        await general_commands.userInfo_command(message)
        await general_commands.rank_command(message)
        await general_commands.commands(message)

        # -----------------------------------------------------------------------------------------------------------
        # MODERATOR / ADMIN COMMANDS
        await admin_commands.position_command(message, has_role)
        await admin_commands.clear_command(message, has_role)

        # -----------------------------------------------------------------------------------------------------------
        # ADMIN HANDLER
        if message.content.startswith('$kick'):
            args = message.content.split()
            ctx = await bot.get_context(message)
            mentioned_members = message.mentions

            if not mentioned_members:
                await message.channel.send("You need to mention user")
                #await message.channel.send("OWNER",ctx.author.top_role )
                #await message.channel.send("Other",member_to_kick.top_role )
                return
            member_to_kick = mentioned_members[0] 

            if len(args) < 2: await message.channel.send("You forgot to add username‼️"); return
            if ctx.author.top_role <= member_to_kick.top_role: await message.channel.send("You can't kick this member"); return
            await kick(ctx, member_to_kick)

    # -----------------------------------------------------------------------------------------------------------
    # Print users in server
    async def print_all_users_roles():
        for guild in bot.guilds: 
            print("\n-----------------------------------------------------------------------------------------------------------")
            print(f"Server: {guild.name}")
            for member in guild.members:
                roles = [role.name for role in member.roles if role.name != "@everyone"]  
                if roles: print(f" ->\t{member.name}: {' | '.join(roles)}")
                else: print(f" ->\t{member.name}: No specific roles")
            print()

    # -----------------------------------------------------------------------------------------------------------
    # Check Utilitys
    async def check_utilitys():
        commands_chategories = {
            "General": bot_utilitys.general_commands,
            "Moderator": bot_utilitys.moderator_commands,
            "Meme": bot_utilitys.meme_commands,
            "Game": bot_utilitys.game_commands,
            "Browser": bot_utilitys.browsers,
        }

        for category, commands in commands_chategories.items():
            print("-----------------------------------------------------------------------------------------------------------")
            print(f"{category}:")
            for command, status in commands.items():
                status_str = "Enabled" if status else "Disabled"
                print(f"  {command}: {status_str}")
            print()

    # -----------------------------------------------------------------------------------------------------------
    # RUN DISCORD BOT "EASY.BOT"
    bot.run(API_KEY)

if __name__ == "__main__":
    if API_KEY: clear(); bot()
