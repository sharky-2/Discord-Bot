import discord
async def test(message):
    if message.content.lower().startswith("$test"):
        
        embed = discord.Embed (
            title = "Steam Game",
            description = "Steam Game",
            color = discord.Color.red()
        )   

        await message.channel.send(embed = embed)
