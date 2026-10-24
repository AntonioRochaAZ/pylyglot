How does it work?
=================

Pylyglot works with simple dictionaries connecting
translated python keywords to their English counterparts.

.. code-block:: python

    dictionary = {
        # Keywords
        "si":           "if",
        "sinonsi":      "elif",
        "sinon":        "else",
        # Logic
        "Faux":         "False",
        "Aucun":        "None",
        "Vrai":         "True",
        ...

Custom Pylyglot file finders and loaders are installed at
the beginning of the python session, taking priority from
python's defaults. This allows python to:

#.  Automatically recognize custom pylyglot file extensions.
#.  Automatically translate the file to regular python
    (using the aforementioned dictionaries) to execute it.

Because these hooks and file executions use python's own built-in 
systems, this integration is seamless, and allows for multilingual
codebases.