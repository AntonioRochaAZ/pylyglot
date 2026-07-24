.. _supported_keywords:

==================
Supported keywords
==================

Dictionary (``dictionary``)
===========================

Most commonly used (must translate)
-----------------------------------

From keyword.kwlist (``from keyword import kwlist``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Logic**:

- if
- elif
- else
- False
- None       
- True
- and
- or
- not
- is
- in
- assert     

**Loops**:

- for
- while
- continue
- break

**try/except/finally**:

- try        
- except     
- raise      
- finally

**imports**:

- from
- import
- as

**Functions/classes/generators**:

- class
- def        
- return     
- lambda
- yield      

**Others**:

- global
- nonlocal
- pass
- async    
- await    
- del
- with

Builtins
~~~~~~~~

All of the built-ins cited in the official python documentation: 
https://docs.python.org/3/library/functions.html,
plus the ``NotImplemented`` built-in.


Other terms
~~~~~~~~~~~ 

- self

Self is not a python keyword in itself, but it deserves a translation due
to its ubiquitous use.

Dunder methods, attributes and constants (mandatory translation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The full list of dunder and special terms (including the optional translation ones)
is taken from this article: 
https://www.pythonmorsels.com/every-dunder-method/

**Common methods**:

- __init__
- __new__
- __del__
- __eq__
- __ne__
- __hash__
- __repr__
- __lt__
- __gt__
- __le__
- __ge__
- __str__
- __bool__
- __int__
- __float__
- __bytes__
- __complex__
- __format__
- __enter__
- __exit__
- __len__
- __iter__
- __getitem__
- __setitem__
- __delitem__
- __contains__
- __reversed__
- __next__
- __call__

**Common attributes and constants**:

- __name__
- __module__
- __file__
- __doc__
- __class__
- __dict__
- __import__
- __builtins__
- __future__
- __version__
- __globals__
- __path__
- __all__
- __main__

**Attribute handling**:

- __getattr__
- __getattribute__
- __setattr__
- __delattr__
- __dir__


**Descriptors**:

- __set_name__
- __get__
- __set__
- __delete__


**Unary operators**:

- __neg__
- __pos__
- __invert__

**Builtin math functions**:

- __divmod__
- __rdivmod__
- __abs__
- __index__
- __round__
- __trunc__
- __floor__
- __ceil__

**Arithmetic operations**:

- __add__
- __sub__
- __mul__
- __truediv__
- __mod__
- __floordiv__
- __pow__
- __matmul__
- __and__
- __or__
- __xor__
- __rshift__
- __lshift__

**Arithmetic operations - right and inplace versions (very similar to previous section)**:

Right versions:

- __radd__
- __rsub__
- __rmul__
- __rtruediv__
- __rmod__
- __rfloordiv__
- __rpow__
- __rmatmul__
- __rand__
- __ror__
- __rxor__
- __rrshift__
- __rlshift__

Inplace versions:

- __iadd__
- __isub__
- __imul__
- __itruediv__
- __imod__
- __ifloordiv__
- __ipow__
- __imatmul__
- __iand__
- __ior__
- __ixor__
- __irshift__

Optional translation
--------------------

Dunder methods, attributes and names (optional translation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Metaprogramming**:

- __prepare__
- __instancecheck__
- __subclasscheck__
- __init_subclass__
- __subclasses__
- __mro_entries__
- __class_getitem__

**Buffers**:

- __buffer__
- __release_buffer__

**Asynchronous operations**:

- __aenter_
- __aexit__
- __aiter__
- __anext__
- __await__

**Library-specific**:

- __post_init__
- __subclasshook__
- __fspath__
- __copy__
- __deepcopy__
- __replace__
- __getnewargs_ex__
- __getnewargs__
- __getstate__
- __setstate__
- __reduce__
- __reduce_ex__
- __sizeof__

**Others**:

- __missing__
- __length_hint__

**Attributes and constants**:

- __slots__      
- __match_args__ 
- __mro__ 
- __bases__
- __wrapped__
- __debug__
- __defaults__
- __kwdefaults__
- __code__
- __closure__
- __qualname__
- __annotations__
- __type_params__
- __static_attributes__
- __firstlineno__
- __func__
- __self__
- __loader__
- __package__
- __spec__
- __cached__
- __traceback__
- __notes__
- __context__
- __cause__
- __suppress_context__
- __objclass__
- __classcell__
- __weakref__
- __origin__
- __args__
- __parameters__
- __unpacked__
- __stdout__
- __stderr__
- __covariant__
- __contravariant__
- __infer_variance__
- __bound__
- __constraints__

Exception dictionary (``exception_dictionary``)
===============================================

Translation of all exceptions is mandatory.

**Exceptions**:

- BaseException
- Exception
- ArithmeticError
- BufferError
- LookupError

**Concrete Exceptions**:

- AssertionError
- AttributeError
- EOFError
- FloatingPointError
- GeneratorExit
- ImportError
- ModuleNotFoundError
- IndexError
- KeyError
- KeyboardInterrupt
- MemoryError
- NameError
- NotImplementedError
- OSError                  
- OverflowError            
- PythonFinalizationError
- RecursionError
- ReferenceError
- RuntimeError
- StopIteration
- StopAsyncIteration
- SyntaxError
- IndentationError
- TabError
- SystemError
- SystemExit
- TypeError
- UnboundLocalError
- UnicodeError
- UnicodeEncodeError
- UnicodeDecodeError
- UnicodeTranslateError
- ValueError
- ZeroDivisionError
- EnvironmentError
- IOError                 
- WindowsError


**OS Exceptions**:

- BlockingIOError          
- ChildProcessError        
- ConnectionError
- BrokenPipeError          
- ConnectionAbortedError
- ConnectionRefusedError
- ConnectionResetError
- FileExistsError
- FileNotFoundError
- InterruptedError
- IsADirectoryError
- NotADirectoryError
- PermissionError
- ProcessLookupError
- TimeoutError

**Warnings**:

- Warning
- UserWarning
- DeprecationWarning          
- PendingDeprecatilonWarning 
- SyntaxWarning
- RuntimeWarning
- FutureWarning
- ImportWarning
- UnicodeWarning
- EncodingWarning
- BytesWarning
- ResourceWarning

**Exception Groups**:

- ExceptionGroup
- BaseExceptionGroup",

Traceback dictionary (``traceback_dictionary``)
===============================================

- Traceback (most recent call last)
- line
- File
- During handling of the above exception, another exception occurred
- The above exception was the direct cause of the following exception
- invalid syntax

Pylyglot internal messages (``pylyglot_internal_messages``)
===========================================================

This dictionary connects keys to their messages. Do not translate the
keys, only the messages. The messages contain variables in brackets
which should not be translated (we'll call ``.format()`` on them when
printing the messages).

Here is the source of pylyglot/languages/en.py, which contain the most
up-to-date version:

.. literalinclude:: ../../../pylyglot/languages/en.py
