try:
    from django.utils.translation import gettext_lazy as _
except ImportError:  # pragma: no cover
    # Allows this module to be executed without Django installed.
    def _(x):
        return x


class GamesBase:
    COMMON_NAMES = {
        "ANW": _("New World"),
        "ALA": _("Lost Ark"),
        "WCT": _("World Of Warcraft Classic TBC"),
        "WCS": _("World Of Warcraft Classic SOM"),
        "WCW": _("World Of Warcraft Classic WOTLK"),
        "POE": _("Path Of Exile"),
        "F14": _("Final Fantasy XIV"),
        "ESO": _("The Elder Scroll Online"),
    }


    def __getstate__(self):
        return None
