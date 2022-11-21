"""Sphinx configuration."""
project = "Pna_Loup_Suivi"
author = "Daniel Thonon"
copyright = "2022, Daniel Thonon"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
