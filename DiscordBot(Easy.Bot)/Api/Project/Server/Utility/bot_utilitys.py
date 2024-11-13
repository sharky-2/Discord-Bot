# -----------------------------------------------------------------------------------------------------------
# General utility commands
general_commands = {
    "$help": False,                                     # Move you to info channel
    "$info": True,                                      # Tell about channel that you are at
    "$botinfo": True,                                   # Tells about bot
    "$invite": True,                                    # Inv others to group
    "$userinfo": True,                                  # Tells about user (roles, name,...)
    "$rank": True,                                      # Tells user rank
    "$commands": True,
}

# -----------------------------------------------------------------------------------------------------------
# Moderator utility commands
moderator_commands = {
    "$pos": True,
    "$ban": False,                                       # Ban user
    "$kick": True,                                      # Kick user
    "$warn": False,                                     # Warn user
    "$clear": True                                      # Clear chat from channel
}

# -----------------------------------------------------------------------------------------------------------
# Memes utility commands
meme_commands = {
    "$joke": True,                                      # Tell random joke
    "$randomfact": False                                # Tell random fact
}

# -----------------------------------------------------------------------------------------------------------
# Game utility commands
game_commands = {
    "$math": True,
    "$word": True,
    "$game steam": True,
    "$game epic": True,
    "$game browser": True
}

# -----------------------------------------------------------------------------------------------------------
browsers = {
    "$wiki": True,
    "$youtube": True,
    "$google": True
}