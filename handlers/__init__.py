# Здесь мы подгружаем хэндлеры из файлов в текущем каталоге
from pathlib import Path
import gettext

# локализация
_locale_dir = Path(__file__).absolute().parent.parent / 'locale'
EN_GETTEXT = gettext.translation('bot_twitt', localedir=str(_locale_dir), languages=['en'])
RU_GETTEXT = gettext.translation('bot_twitt', localedir=str(_locale_dir), languages=['ru'])
RU_GETTEXT.install()

from . import admin
from . import general_commands
from . import menu
from . import default_handler
