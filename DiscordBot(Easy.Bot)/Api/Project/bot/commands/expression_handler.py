from Api.Project.Server.other import expressions
from Api.Project.Server import setting
import asyncio
# -----------------------------------------------------------------------------------------------------------
# Greeding
async def handle_greetings(message):
    if any(message.content.lower().startswith(greeting) for greeting in expressions['greetings']):
        bot_message = await message.channel.send(f"{message.content.title()} {message.author.mention} 😊")
        if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(10); await message.delete(); await bot_message.delete()

# -----------------------------------------------------------------------------------------------------------
# Farewell
async def handle_farewells(message):
    if any(message.content.lower().startswith(farewell) for farewell in expressions['farewells']):
        bot_message = await message.channel.send(f"{message.content.title()} {message.author.mention} ✌️")
        if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(10); await message.delete(); await bot_message.delete()