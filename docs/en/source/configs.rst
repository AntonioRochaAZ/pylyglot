.. _configs:

Settings (configs)
==================

.. seealso::
    :ref:`How to change settings through the command line <config_options>`

- ``verbose``: whether to print extra information when pylyglot is running. Default: False.
- ``default_language``: Default langauge for translations (when not specified and it can't be
  inferred from the extension), running the console, etc. Default: "en".
- ``input_encoding``: Default encoding considered for reading the file being translated or run. Default: "utf-8".
- ``encoding_errors``: Default value for the ``errors`` keyword of the decode method of bytes object 
  (used during reading of a file which will be translated or run). Default: "strict".
- ``output_encoding``: Default encoding considered for generating the translated file. Default: "utf-8".
