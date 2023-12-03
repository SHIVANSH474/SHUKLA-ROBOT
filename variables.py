# https://github.com/Imshukla87/SHUKLA-ROBOT
# https://github.com/Imshukla87


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 29308061  # Get this value from my.telegram.org/apps
    API_HASH = "462de3dfc98fd938ef9c6ee31a72d099"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://ierjlkr:OG4dxzO67Zret3Zii43Hhvujkg89WVry0n9KsHE@karma.db.elephantsql.com/ierjlkr"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002018556839
    MESSAGE_DUMP = -1001766825642

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "mastiwithfriendsx"
    SUPPORT_ID = -1001766825642

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "2323839365:AAFgfdadqawlfdsM7slOa33eM_ghop"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6919199044
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True
    BAN_STICKER = ""

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
