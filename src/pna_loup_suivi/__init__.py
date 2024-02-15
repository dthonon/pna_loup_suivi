"""Pna_Loup_Suivi."""

import gettext
from importlib.metadata import version
from pathlib import Path


# Change here if project is renamed and does not equal the package name
dist_name = "pna_loup_suivi"
__version__ = version(dist_name)

# Install gettext for any file in the application
localedir = Path(__file__).resolve().parent / "locale"
gettext.bindtextdomain(dist_name, str(localedir))
gettext.textdomain(dist_name)
_ = gettext.gettext
