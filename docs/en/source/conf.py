# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Pylyglot'
copyright = '2026, Antonio ROCHA AZEVEDO'
author = 'Antonio ROCHA AZEVEDO'
release = '2026'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.autosectionlabel',
    'sphinx.ext.viewcode', 'sphinx.ext.todo'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Pylyglot"
html_favicon = '_static/favicon.ico'
html_theme = 'furo'
html_static_path = ['_static']
# conf.py
html_theme = "furo"
html_theme_options = {
    "light_css_variables": {
        # "color-background-primary": "#fdfdfd",
        # "color-background-secondary": "#f0f0f0",
    },
    "dark_css_variables": {
        "color-background-primary": "#24283b",
        "color-background-secondary": "#1f2335",
    },
}
pygments_style = "dracula"
pygments_dark_style = "dracula"
