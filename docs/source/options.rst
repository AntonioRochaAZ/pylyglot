.. _clo:

Command Line Options
====================

Pylyglot is invoked as a module:

.. code-block:: bash

    python -m pylyglot [options] <file> [destination]

Running a file
--------------

With no other option, pylyglot translates ``<file>`` to Python and runs it
as ``__main__``:

.. code-block:: bash

    python -m pylyglot portuguese_module.pt_br.py


.. _translate_option:

``--translate``
---------------

Translates a file (or a whole directory tree) instead of running it.

.. code-block:: bash

    python -m pylyglot --translate=<destination_language_code> <source> <destination>

- ``<source>``: file or directory to translate.
- ``<destination>``: output file or directory.
- ``<output_language>`` is optional if it can be inferred from
  ``<destination>``'s extension (e.g. ``.fr.py``). If it can't be inferred,
  pylyglot falls back to your configured default language 
  (see the :ref:`"Settings (configs)" <configs>` section) and warns.
- If ``<source>`` is a directory, every ``.py`` file inside it is
  translated recursively, preserving the directory structure, with each
  output file renamed to carry the ``.<destination_language_code>.py`` suffix
  (or plain ``.py`` when translating to English).

``--console``
-------------

Launches an interactive console in the given language:

.. code-block:: bash

    python -m pylyglot --console=<language_code>


If no language is given (``--console`` alone), the console uses your default language
(see the :ref:`"Settings (configs)" <configs>` section).

.. note::
    ``--translate`` and ``--console`` are mutually exclusive.

.. _config_options:

Configuration options
---------------------

.. seealso::
    :ref:`This page with the current supported settings. <configs>`

Pylyglot has a few settings that can be changed with the following
command line options (these exit immediately after running: no other option is processed
alongside them):

``--setconfig <key>=<value>``
    Sets a configuration option (e.g. default_language).

``--getconfig``
    Prints the current complete configuration dictionary as JSON.

``--getconfigpath``
    Prints the path to the configuration file.

``--resetconfig``
    Resets all settings in the configuration file to defaults.

.. 
    Other flags
    -----------

    Any additional ``--key=value`` (or bare ``--key``, which sets the key to None) 
    argument is stored as a run option and passed through to translation/execution: 
    for example ``--verbose=true`` or ``--encoding=utf-8``.

    .. TODO: list all recognized pass-through options (encoding, errors,
    verbose, default_language, ...) once finalized.
