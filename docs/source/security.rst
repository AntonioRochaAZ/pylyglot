.. _security:

Security
========

.. danger::
    Pylyglot may expose you to security risks **if** you are running
    untrusted code from languages you don't understand, or if you 
    have name clashes that could trigger the wrong function call.
    
    Treat ``python -m pylyglot`` exactly like ``python``:
    never run, translate, or import untrusted files.


Simple example
--------------

For example, the following portuguese python code:

.. code-block:: python
    
    de utils importar soma

Would try to import object "soma" from module "utils". However, "soma" means "sum"
in Portuguese (the name of the python builtin),
and the translation of this line would end up giving 
``from utils import sum``, which would be
an ``ImportError`` if the ``sum`` object doesn't exist in the module 
**or worse: a different function could be executed altogether, which can
expose you to security threats!**

.. tip::
    You can always translate files and codebases to plain python
    without running them at all with the ``--translate`` option
    (read more about it :ref:`here <translate_option>`). However,
    note that this does not translate strings, comments etc.

.. _security_name_clashing:

Automatic name clash handling
-----------------------------

Originally, if a pylyglot file contained a variable name which clashes
with an english keyword (or a destination language keyword, if translating
from one language to another), its name would be altered during translation to avoid
syntax errors (for example ``if --> if0_``).
        
Although the automatic renaming ensured that the name did not exist in
the module, it could eventually cause issues with names from imported modules
(for example through ``from module import *``). Because of this, this feature
could silently cause unintended behaviour or even expose the user to security
risks. It is still possible to bypass this with an option. 

Considerations
--------------

- **No sandboxing.** Translation only rewrites keywords/identifiers before
  compiling — the resulting code runs with the exact same privileges as
  any other Python script (file access, network, subprocess, etc.).
  Pylyglot adds *no* isolation on top of the interpreter.

- **You may not be able to read the risk.** If you don't speak the source
  language, you can't audit the file before running it. Translating it to
  your language first (``--translate``) only converts keywords/names —
  comments, docstrings, and string literals (where malicious intent is
  often hidden) are left untouched.

- **Name-clash fallback can silently misdirect imports.** As described
  above, a translated import can resolve to the wrong object if a
  translated keyword collides with a real name in the target module —
  in the worst case, executing unintended code. Always verify
  ``# pylyglot: keep`` lines by hand, since they're regular Python and
  bypass translation entirely — including any safety review you'd
  otherwise expect the translator to catch as well.

  .. todo::
      Add a regular expression to identify this, potentially.

- **Import hooks are process-wide.** Installing Pylyglot's hooks affects
  ``sys.path_hooks``/``sys.meta_path`` for the whole interpreter session,
  not just files you explicitly run — any subsequent import (yours or a
  library's) is subject to the same suffix/ambiguity resolution.

- **Homoglyph / lookalike identifiers.** Because translation matches
  keywords by dictionary lookup, visually similar Unicode characters
  could be used to disguise a variable or function name from the
  translated dictionary — a general Python risk, but worth extra caution
  here since you're already trusting the translation step.