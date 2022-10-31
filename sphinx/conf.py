# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx-Test'
copyright = '2022, Toru Yoshihara'
author = 'Toru Yoshihara'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

# My additional settings
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "show_nav_level": 2,
    "icon_links": [
        {
            "name": "GitHub",
            "url": (
                f"https://github.com/toru-ver4/Sphinx-Test"
            ),
            "icon": "fab fa-github",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/toru_ver15",
            "icon": "fab fa-twitter",
        },
    ],
}
extensions = ['sphinx.ext.mathjax', 'sphinx.ext.githubpages']
