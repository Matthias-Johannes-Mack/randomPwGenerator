# password_generator/constants.py
# Import gettext module
import gettext
from utils.app_utils import store_locale, restart_application, load_settings


def set_gettext_locale(new_locale):
    # Set the local directory
    appname = "base"
    localedir = "./locales"
    print(new_locale)
    # Set up Gettext
    en_i18n = gettext.translation(
        appname, localedir, fallback=False, languages=[new_locale]
    )
    # Create the "magic" function
    en_i18n.install()
    _ = en_i18n.gettext


def update_gettext_locale(new_locale):
    store_locale(new_locale)
    restart_application()


settings = load_settings()
current_code = settings["locale"]
set_gettext_locale(current_code)

# GUI Constants
VERSION = "V1.0.0"
WINDOW_TITLE = _("Password Generator ") + VERSION
AUTHOR = "Matthias J. Mack"

# Label descriptors
LABEL_LENGTH = _("Password length:")
LABEL_GENERATED_PASSWORD = _("Generated password:")
LABEL_PASSWORD_LENGTH = _("Password length:")
LABEL_INCLUDE_UPPERCASE = _("Include uppercase")
LABEL_INCLUDE_DIGITS = _("Include digits")
LABEL_INCLUDE_SPECIAL_CHARS = _("Include special characters")
LABEL_MSSQL = _("MSSQL password policy")

# Menu label descriptors
LABEL_ABOUT = _("About")
LABEL_FILE = _("File")
LABEL_SETTINGS = _("Settings")
LABEL_EXIT = _("Exit")
LABEL_HELP = _("Help")

# Button descriptors
BUTTON_GENERATE_PASSWORD = _("Generate")

# Message descriptors
ABOUT_MESSAGE = WINDOW_TITLE + _("\n\n\n\nDeveloped by ") + AUTHOR
CLIPBOARD_MESSAGE = _("Password copied to clipboard!")

# Default Password Length
DEFAULT_PASSWORD_LENGTH = 16

EMPTY_STRING = ""
DASH = "|"
COPY_SYMBOL = "\u2398"

# Settings for the animation
GENERATION_DELAY = 5
ANIMATION_SIZE = 50

# Style constants
FONT_NAME = "Helvetica"
FONT_SIZE = 10

# I118N
LANGUAGE_ARRAY = ["English", "German", "Spanish", "French", "Italian", "Chinese"]
COUNTRY_CODE_ARRAY = ["en", "de", "es", "fr", "it", "cn"]
DEFAULT_WINDOW_SIZE = "570x310"
WINDOW_SIZES_ARRAY = {
    "en": "515x310",
    "de": "505x310",
    "es": "565x310",
    "fr": "575x310",
    "it": "570x310",
    "cn": "480x310",
}

# MSSQL specific settings
MSSQL_SPECIAL_CHARS = "!$#%"
