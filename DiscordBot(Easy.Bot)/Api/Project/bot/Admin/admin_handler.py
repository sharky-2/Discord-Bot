import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = "$", intents = intents)

# -----------------------------------------------------------------------------------------------------------
# Kick user
@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f"`{member}` has been kicked!")