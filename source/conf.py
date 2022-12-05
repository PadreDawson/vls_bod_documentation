# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'VLS Board Documentation'
copyright = '2022, Valley Lutheran School'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
extensions = [
    "sphinx_design",
    # 'sphinx_rtd_theme',
]

# html_theme = "sphinx_rtd_theme"
html_theme = "pydata_sphinx_theme"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_logo = '_images/valley_logo4.png'
html_title = 'Valley Lutheran School'
templates_path = ['_templates']
html_css_files = ['css/custom.css',]

html_theme_options = {
    "logo": {
        "text": 'Valley Lutheran School',
        # "link": "https://www.vlscrusaders.org/",
        },
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links", "theme-switcher"],
    "navbar_persistent": ["search-button"],
    "show_toc_level": 2,
    "primary_sidebar_end": ['page-toc'],
    "footer_items": ['copyright', 'theme-version'],
    
}
html_context = {
   "default_mode": "light"
}
