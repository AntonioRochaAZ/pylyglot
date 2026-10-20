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
   * - ``ar``
     - Modern Standard Arabic
     - Complete (AI generated)
     - Contributor needed
   * - ``cs``
     - Czech
     - Complete (AI generated)
     - Contributor needed
   * - ``da``
     - Danish
     - Complete (AI generated)
     - Contributor needed
   * - ``de``
     - German
     - Complete (AI generated)
     - Contributor needed
   * - ``en``
     - English
     - Complete
     - Used for default internal pylyglot messages.
   * - ``es``
     - Spanish
     - Complete (AI generated)
     - Contributors welcome, verified by a human.
   * - ``fi``
     - Standard Finnish (suomi)
     - Complete (AI generated)
     - Contributor needed
   * - ``fr``
     - French
     - Complete
     - Mostly manually translated. Fully verified.
   * - ``ha``
     - Hausa
     - Complete (AI generated)
     - Contributor needed
   * - ``hi``
     - Hindi
     - Complete (AI generated)
     - Contributor needed, "uses Devanagari script"
   * - ``is``
     - Icelandic
     - Complete (AI generated)
     - Contributor needed
   * - ``it``
     - Italian
     - Complete (AI generated)
     - Contributor needed
   * - ``ja``
     - Japanese
     - Complete (AI generated)
     - Contributor needed
   * - ``ko``
     - Korean
     - Complete (AI generated)
     - Contributor needed, "Hangul script"
   * - ``nb``
     - Norwegian Bokmål
     - Complete (AI generated)
     - Contributor needed
   * - ``nl``
     - Dutch
     - Complete (AI generated)
     - Contributor needed
   * - ``pl``
     - Polish
     - Complete (AI generated)
     - Contributor needed
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
   * - ``ru``
     - Russian
     - Complete (AI generated)
     - Contributor needed
   * - ``sv``
     - Swedish
     - Complete (AI generated)
     - Contributor needed
   * - ``sw``
     - Swahili
     - Complete (AI generated)
     - Contributor needed
   * - ``uk``
     - Ukranian
     - Complete (AI generated)
     - Contributor needed
   * - ``yo``
     - Yoruba
     - Complete (AI generated)
     - Contributor needed
   * - ``zh``
     - Simplified Chinese
     - Complete (AI generated)
     - Contributor needed

Detecting a file's language
---------------------------

Pylyglot infers a file's language from its filename suffix (e.g.
``.pt_br.py``). If a file has no recognized language suffix, it's treated
as plain Python and passed through unchanged.