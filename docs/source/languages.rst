.. _available_languages:

Available Languages
===================

Each supported language lives as a module inside ``pylyglot/languages/``,
named with its language code (e.g. ``pt_br.py``). A language module exposes
multiple different dictionaries. Translations may be more or less complete 
according to the language.

..
    ``dictionary``
        Maps translated keywords/builtins to their English Python equivalents
        (e.g. ``{"importar": "import", "para": "for"}``).

    ``traceback_dictionary``
        Additional mappings used only when rewriting tracebacks and error
        messages (e.g. exception class names, "Traceback (most recent call
        last)").

Currently supported
-------------------

.. list-table::
   :header-rows: 1

   * - Code
     - Language
     - Status
   * - ``pt``
     - Portuguese (default, points to ``pt_br``)
     - Mostly complete
   * - ``pt_br``
     - Portuguese (Brazil)
     - Mostly complete
   * - ``fr``
     - Portuguese (Brazil)
     - In progress

Detecting a file's language
---------------------------

Pylyglot infers a file's language from its filename suffix (e.g.
``.pt_br.py``). If a file has no recognized language suffix, it's treated
as plain Python and passed through unchanged.