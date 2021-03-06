##########################################################
#                                                        #
#                 ¡ This is a template !                 #
#                                                        #
#   Make sure to edit it with your preferred settings!   #
#              And to place it in the /data              #
#                subdirectory of the bot,                #
#        without the 'template_' part of the name        #
#                                                        #
##########################################################
"""
Settings and options for the bot.
---
"""


# The prefix for the bot (str). Define a list of stings for multiple prefixes.
# ie: `["?", "!", "pls "]`
command_prefix = ["mb? ", "mb?", "Mb? ", "Mb?"]

# The prefix to use for display purposes (ex: status message).
display_prefix = "mb?"


# The roles to give to new members, per guild.
# {
#     guild_id: [
#         role_id,
#         role_id,
#         ...
#     ],
#     ...
# }
autoroles = {}


# The self-assingnable roles, per guild.
# {
#     guild_id: [
#         role_id,
#         role_id,
#         ...
#     ],
#     ...
# }
selfroles = {}
