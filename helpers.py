from emoji import EmojiID
from role import Role


def get_role_id(emoji):
    if emoji.id == EmojiID.VALHEIM:
        return Role.VALHEIM
    elif emoji.id == EmojiID.VALORANT:
        return Role.VALORANT
    elif emoji.id == EmojiID.GENSHIN:
        return Role.GENSHIN
    elif emoji.id == EmojiID.PHASMO:
        return Role.PHASMO
    elif emoji.id == EmojiID.KINGS_RAID:
        return Role.KINGS_RAID
    elif str(emoji) == '🍪':
        return Role.COOKIE_CLICKER
    else:
        return None
