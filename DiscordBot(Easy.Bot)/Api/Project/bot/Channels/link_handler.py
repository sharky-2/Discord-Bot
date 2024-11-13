import asyncio
from Api.Project.Server import setting
from Api.Project.Server.Utility import link_utilitys
from Api.Project.Server.other import channel_responses

# -----------------------------------------------------------------------------------------------------------
# Links handler
async def handle_links(message):
    forbiden_channels = link_utilitys.links.get(message.channel.name[1:], False)
    if message:
        if not forbiden_channels:

            # Remove link if https
            if message.content.startswith('https://') and not message.content.endswith(('jpg', 'png', 'gif', 'webp')):
                try:
                    # Message
                    await message.delete()
                    bot_message = await message.channel.send(
                        f"**⚠️ Link Forbiden\n**\n"
                        f"{message.author.mention} You can't paste link in this channel"
                    )
                    
                    # Delete Message
                    if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await bot_message.delete()
                except: pass
    else: pass