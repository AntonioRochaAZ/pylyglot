.. _contributing:

Contributing
=============

We are looking for contributors for revising translations which
were AI generated (currently all except for French, Portuguese and English),
propose bug fixes and propose translations for new languages!

AI disclaimer
-------------

Contributors MUST acknowledge in their issue if AI was used at any point in
their contribution and how. :ref:`Check our dedicated page on the use of AI <ai>` to
see how the use of AI is allowed.


Adding a new language
---------------------

1.  Create a new module under ``pylyglot/languages/``, named with the
    language's code (e.g. ``fr.py`` for French). We suggest the
    `ISO 639-1 Code <https://www.loc.gov/standards/iso639-2/php/code_list.php>`_.
    For variants of a language, use an underscore to separate the main language
    code from the variant tag. For example, for brazilian (br)
    portuguese (pt) you should write ``pt_br`` and not ``pt-br``.

2.  Define the following dictionaries (see pylyglot/languages/pt_br.py for the most complete example): 
    
    - ``dictionary`` : largest mapping of translated keywords to their English
      Python equivalents.
    - ``exception_dictionary``: mapping exception names to their original version.
    - ``traceback_dictionary``: for error-message translations.
    - ``pylyglot_internal_messages``: mapping of internal pylyglot keys to their
      messages. Note that these strings contain terms in brackets, which will be
      later formatted with "format". Do not change the name of those variables.

3.  Add the following lines to the en of your script to integrate the exception
    messages to both the regular dicitonary and the traceback one:

    .. code-block:: python
        
        dictionary.update(exception_dictionary)
        traceback_dictionary.update({v: k for k, v in exception_dictionary.items()})


4.  Add a short entry for the language in :doc:`languages`.

.. note::
    Defining "informal" languages (such as "pirate english" or variants
    using slang) is permitted. 
    However, no slurs or derogatory terms will be accepted.  


Running tests
-------------

Run the tests using `pytest <https://pypi.org/project/pytest/>`_
and make sure there are no errors before opening a pull request.
Simply run "``pytest``" from the base folder.
