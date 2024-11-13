# -----------------------------------------------------------------------------------------------------------
# Imports
import random as rng
import asyncio
import discord
from discord import Embed
from Api.Project.Server.Utility import bot_utilitys
from Api.Project.Server import setting
from Api.Project.Server.Game_channel import random_words

# -----------------------------------------------------------------------------------------------------------
# Global
choosen_word = []
current_display = [] 
tries = 0

# -----------------------------------------------------------------------------------------------------------
# Generate word
async def randomWord(message):
    # Check command
    botCommands = bot_utilitys.game_commands.get(message.content.lower(), False)
    if message.content.lower().startswith("$word") and message.content != "$clear":
        if "guess" in message.channel.name:
            if botCommands:
                # Choose word
                word = random_words.random_word
                choosen_word.clear()
                random_word = rng.choice(word)
                choosen_word.append(random_word) 
                
                # Set up word
                global current_display, tries
                current_display = ['_' for _ in random_word] 
                tries = 0  
                
                print(random_word, choosen_word)

                embed = Embed(
                    title = f"🔤 New Word Chosen",
                    description = f"Current state: `{' '.join(current_display)}`",
                    color = discord.Color.blue()
                )
                await message.channel.send(embed=embed)
                
            # Command turned off
            else:
                bot_message = await message.channel.send(
                    f"**❌ Command Disabled\n**\n"
                    f"The command `{message.content}` is currently turned **OFF**."
                    "Try again later."
                )
                if setting.settings.get("delete_commands_messages", False):
                    await asyncio.sleep(5)
                    await message.delete()
                    await bot_message.delete()
        else:
            bot_message = await message.channel.send(
                f"**⚠️ Wrong Channel\n**\n"
                f"To use `{message.content}`, please go to the **#📃guess-a-word** channel."
            )
            if setting.settings.get("delete_commands_messages", False): await asyncio.sleep(5); await message.delete(); await bot_message.delete()

# -----------------------------------------------------------------------------------------------------------
# User guessing word
async def guessWord(message):
    global choosen_word, tries, current_display
    if len(choosen_word) != 0:
        if "guess" in message.channel.name:
            if message.content != "$clear" and message.content != "$word":
                guess = message.content.lower()

                # Guesses full word
                if guess == choosen_word[0]: 
                    await message.channel.send(
                        f"✅ You have guessed the word '{choosen_word[0]}' in `{tries}` tries. \nType the command `$word` again to play."
                    )
                    choosen_word.clear()
                    current_display.clear()
                    return 

                # Guessed letter
                elif len(guess) == 1:
                    if guess in choosen_word[0]:  
                        for index, letter in enumerate(choosen_word[0]):
                            if letter == guess:
                                current_display[index] = guess
                        tries += 1
                        await message.channel.send(
                            f"✅ Correct! Current state: `{' '.join(current_display)}`"
                        )
                    else:
                        tries += 1
                        await message.channel.send(
                            f"❌ Incorrect guess. So far failed tries: `{tries}`. \nCurrent state: `{' '.join(current_display)}`"
                        )
                else:
                    tries += 1
                    await message.channel.send(
                        f"❌ Invalid input. Please guess a single letter or the full word. So far failed tries: `{tries}`. \nCurrent state: `{' '.join(current_display)}`"
                    )

                # Tell tried each 10 failed tries
                if tries % 10 == 0:
                    await message.channel.send(f"❌ Total failed tries: `{tries}`")

                # End game after 100 tries
                if tries >= 100: 
                    await message.channel.send(
                        f"❌ You've reached the maximum tries. The correct word was '{choosen_word[0]}'. \nType the command `$word` again to play."
                    )
                    choosen_word.clear() 
                    current_display.clear() 
                    tries = 0 
