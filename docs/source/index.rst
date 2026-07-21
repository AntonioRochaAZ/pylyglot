Pylyglot: write and run python code on your native language
===========================================================

`Github repository <https://github.com/AntonioRochaAZ/pylyglot>`_

[insert image here]

Pylyglot is an extremely simple python package with no dependencies
(other than python itself) which allow you to write "python" code
with keywords from your language. Running it is as simple as running: 

``python -m pylyglot your_module.py``

Pylyglot also handles importing multilingual modules gracefully. 

.. figure:: _static/README_example.png


With the `Pylyglot VSCode extension <>`_, syntax highlighting is also available for all
supported languages. The language is automatically recognized by the file extension: 
``.language_code.py`` (e.g. portuguese_module **.pt.py**).

.. toctree::

    Installation <installation>
    Features <features>
    Command line options <features>
    Available languages <languages>
    Security <security>
    Settings (configs) <configs>
    Contributing <contributing>
    Contributors <contributors>