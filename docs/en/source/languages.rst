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
     - Comment
   * - ``de``
     - German
     - Contributor needed
     - AI generated
   * - ``en``
     - English
     - Complete
     - For internal pylyglot messages.
   * - ``es``
     - Spanish
     - Verification in progress
     - AI generated
   * - ``fr``
     - French
     - Verification in progress
     - Manual + AI generated
   * - ``it``
     - Italian
     - Contributor needed
     - AI generated
   * - ``jp``
     - Japanese
     - Contributor needed
     - AI generated
   * - ``pt``
     - Portuguese
     - Complete
     - Default, points to ``pt_br``
   * - ``pt_br``
     - Portuguese (Brazil)
     - Complete
     - Mostly manually translated. Fully verified.
   * - ``pt_rj``
     - Portuguese (Rio de Janeiro)
     - In progress
     - Informal (contains slang)

Detecting a file's language
---------------------------

Pylyglot infers a file's language from its filename suffix (e.g.
``.pt_br.py``). If a file has no recognized language suffix, it's treated
as plain Python and passed through unchanged.