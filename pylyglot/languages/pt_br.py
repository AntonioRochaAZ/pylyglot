dictionary = {
    # keyword.kwlist (from keyword import kwlist)
    # if/else    
    "se":         "if",
    "senãose":    "elif",
    "senão":      "else",
    # logic:
    "Falso":      "False",
    "Nenhum":     "None",       
    "Verdadeiro": "True",
    "e":          "and",
    "ou":         "or",
    "não":        "not",
    "é":          "is",
    "em":         "in",
    "assegurar":    "assert",     
    # Loops:
    "paracada":    "for",
    "enquanto":   "while",
    "continuar":  "continue",
    "quebrar":    "break",
    # try/except/finally
    "tentar":     "try",        
    "exceto":     "except",     
    "levantar":   "raise",      
    "finalmente": "finally",
    # imports
    "de":         "from",
    "importar":   "import",
    "como":       "as",
    # Functions/classes/generators
    "classe":     "class",
    "def":        "def",        
    "retornar":   "return",     
    "lambda":     "lambda",
    "gerar":   "yield",      
    # Others:
    "global":     "global",
    "nãolocal":   "nonlocal",
    "passar":     "pass",
    "asinc":    "async",    
    "esperar":    "await",    
    "del":        "del",
    "com":        "with",

    #builtins: https://docs.python.org/3/library/functions.html
    #A
    "abs":  "abs",
    "aiter":  "aiter", #
    "todos":  "all",
    "apróx":  "anext",#
    "algum":  "any",
    "ascii":  "ascii",
    #B
    "bin": "bin",#
    "bool":         "bool",
    "pontodeparada":         "breakpoint",#
    "matrizbytes":  "bytearray",
    "bytes":        "bytes",
    #C
    "chamável":    "callable",
    "car":    "chr",
    "métododeclasse":    "classmethod",
    "compilar":    "compile",
    "complexo":     "complex",
    #D
    "delatr": "delattr",
    "dicio":        "dict",
    "dir":        "dir",#
    "divmod": "divmod",#
    #E
    "enumerar": "enumerate",
    "aval": "eval",
    "exec": "exec",
    #F
    "filtrar": "filter",
    "flut":    "float",
    "format":  "format",
    "conjfixo":    "frozenset",#
    #G
    "buscatr": "getattr",
    "globais": "globals",
    #H
    "tematr": "hasattr",
    "hash": "hash",
    "ajuda": "help",
    "hex": "hex",
    #I
    "id": "id",
    "entrada": "input",#
    "int":          "int",
    "éinstância": "isinstance",
    "ésubclasse": "issubclass",
    "iter": "iter",#
    #L
    "tamanho": "len",
    "lista":        "list",
    "locais": "locals",
    #M
    "mapear": "map",
    "max": "max",
    "visdememória": "memoryview",#
    "min": "min",
    #N
    "próximo": "next",
    #O
    "objeto":       "object",
    "oct":       "oct",
    "abrir":       "open",
    "ord":       "ord",
    #P
    "pot":       "pow",
    "imprimir":   "print",
    "propriedade":   "property",
    #R
    "intervalo":    "range",
    "repr":    "repr",#
    "inverter":    "reversed",
    "arred":    "round",
    #S
    "conj":         "set",
    "defatr":          "setattr",
    "fatia":          "slice",
    "ordenar":          "sorted",
    "métodoestático":          "staticmethod",
    "txt":          "str",
    "soma":          "sum",
    "super":          "super",
    #T
    "tupla":         "tuple",
    "tipo":         "type",
    #V
    "vars": "vars",
    #Z
    "zip": "zip",

    #Others:
    "si": "self",
 
    #Dunder methods: https://www.pythonmorsels.com/every-dunder-method/#cheat-sheet
    "__inic__":                 "__init__",
    "__new__":                  "__new__",
    "__del__":                  "__del__",
    "__ig__":                   "__eq__",
    "__desig__":                "__ne__",
    "__hash__":                 "__hash__",
    "__repr__":                 "__repr__",
    "__menq__":                 "__lt__",
    "__maiq__":                 "__gt__",
    "__menig__":                "__le__",
    "__maiig__":                "__ge__",
    "__txt__":                  "__str__",
    "__bool__":                 "__bool__",
    "__int__":                  "__int__",
    "__flut__":                 "__float__",
    "__bytes__":                "__bytes__",
    "__complexo__":             "__complex__",
    "__format__":               "__format__",
    "__entrar__":               "__enter__",
    "__sair__":                 "__exit__",
    "__tamanho__":              "__len__",
    "__iter__":                 "__iter__",
    "__buscaritem__":           "__getitem__",
    "__defitem__":              "__setitem__",
    "__delitem__":              "__delitem__",
    "__contém__":               "__contains__",
    "__invertido__":            "__reversed__",
    "__próximo__":              "__next__",
    "__faltando__":             "__missing__",
    "__dica_tamanho__":         "__length_hint__",
    "__chamar__":               "__call__",

    # Arithmetic operations:
    "__som__":                  "__add__",
    "__sub__":                  "__sub__",
    "__mul__":                  "__mul__",
    "__divver__":               "__truediv__",
    "__res__":                  "__mod__",
    "__divchão__":              "__floordiv__",
    "__pot__":                  "__pow__",
    "__mulmat__":               "__matmul__",
    "__e__":                    "__and__",
    "__ou__":                   "__or__",
    "__ouexc__":                "__xor__",
    "__deslocdir__":            "__rshift__",
    "__deslocesq__":            "__lshift__",
    # Right versions:
    "__somdir__":                  "__radd__",
    "__subdir__":                  "__rsub__",
    "__muldir__":                  "__rmul__",
    "__divverdir__":               "__rtruediv__",
    "__resdir__":                  "__rmod__",
    "__divchãodir__":              "__rfloordiv__",
    "__potdir__":                  "__rpow__",
    "__mulmatdir__":               "__rmatmul__",
    "__edir__":                    "__rand__",
    "__oudir__":                   "__ror__",
    "__ouexcdir__":                "__rxor__",
    "__deslocdirdir__":            "__rrshift__",
    "__deslocesqdir__":            "__rlshift__",
    # Inplace versions:
    "__isom__":                  "__iadd__",
    "__isub__":                  "__isub__",
    "__imul__":                  "__imul__",
    "__idivver__":               "__itruediv__",
    "__ires__":                  "__imod__",
    "__idivchão__":              "__ifloordiv__",
    "__ipot__":                  "__ipow__",
    "__imulmat__":               "__imatmul__",
    "__ie__":                    "__iand__",
    "__iou__":                   "__ior__",
    "__iouexc__":                "__ixor__",
    "__ideslocdir__":            "__irshift__",
    # unary:
    "__neg__":                  "__neg__",
    "__pos__":                  "__pos__",
    "__invert__":               "__invert__",
    # Builtin math functions:
    "__divres__":               "__divmod__",
    "__divresdir__":              "__rdivmod__",
    "__abs__":                  "__abs__",
    "__índice__":                "__index__",
    "__arred__":                "__round__",
    "__trunc__":                "__trunc__",
    "__chão__":                "__floor__",
    "__teto__":                 "__ceil__",
    # Attribute
    "__buscatr__":              "__getattr__",
    "__buscatributo__":         "__getattribute__",
    "__defatr__":              "__setattr__",
    "__delatr__":              "__delattr__",
    "__dir__":                  "__dir__",
    # Metaprogramming section..... TODO

    #Dunder attributes/constants: https://www.pythonmorsels.com/every-dunder-method/
    "__nome__": "__name__",
    "__módulo__": "__module__",
    "__doc__": "__doc__",
    "__classe__": "__class__",
    "__dicio__": "__dict__",
    "__slots__": "__slots__",               # TODO
    "__match_args__": "__match_args__",     # TODO
    "__orm__": "__mro__", # Method Resolution Order
    "__bases__": "__bases__",
    "__arquivo__": "__file__",
    "__embrulhados__": "__wrapped__",
    "__versão__": "__version__",
    "__todos__": "__all__",
    "__debug__": "__debug__",
    # Functions... TODO

    #Other builtins
    "NãoImplementado": "NotImplemented",

    # Exceptions:
    "ExceçãoBase":              "BaseException",
    "Exceção":                  "Exception",
    "ErroDeAritmética":         "ArithmeticError",
    "ErroDeBuffer":             "BufferError",
    "ErroDeConsulta":           "LookupError",
    # Concrete Exceptions:
    "ErroDeAfirmação":          "AssertionError",
    "ErroDeAtributo":           "AttributeError",
    "ErroDeFimDeArquivo":       "EOFError",
    "ErroDePontoFlutuante":     "FloatingPointError",
    "SaídaDeGerador":           "GeneratorExit",
    "ErroDeImportação":         "ImportError",
    "ErroDeMóduloNãoEncontrado": "ModuleNotFoundError",
    "ErroDeÍndice":             "IndexError",
    "ErroDeChave":              "KeyError",
    "InterrupçãoDeTeclado":     "KeyboardInterrupt",
    "ErroDeMemória":            "MemoryError",
    "ErroDeNome":               "NameError",
    "ErroNãoImplementado":      "NotImplementedError",
    "ErroDeSO":                 "OSError",                  #
    "ErroDeOveflow":            "OverflowError",            
    "ErroDeFinalizaçãoPython":  "PythonFinalizationError",
    "ErroDeRecursão":           "RecursionError",
    "ErroDeReferência":         "ReferenceError",
    "ErroDeExecução":           "RuntimeError",
    "PararIteração":            "StopIteration",
    "PararIteraçãoAsinc":       "StopAsyncIteration",
    "ErroDeSintaxe":            "SyntaxError",
    "ErroDeIndentação":         "IndentationError",
    "ErroDeTab":                "TabError",
    "ErroDoSistema":            "SystemError",
    "SaídaDoSistema":           "SystemExit",
    "ErroDeTipo":               "TypeError",
    "ErroDeVariávelNãoDefinida": "UnboundLocalError",
    "ErroDeUnicode":            "UnicodeError",
    "ErroDeCodificaçãoUnicode": "UnicodeEncodeError",
    "ErroDeDecodificaçãoUnicode": "UnicodeDecodeError",
    "ErroDeTraduçãoUnicode":    "UnicodeTranslateError",
    "ErroDeValor":              "ValueError",
    "ErroDeDivisãoPorZero":     "ZeroDivisionError",
    "ErroDeAmbiente":           "EnvironmentError",
    "ErroDeIO":                 "IOError",                 
    "ErroDoWindows":            "WindowsError",
    # OS Exceptions:
    "ErroDeIOBloqueador":       "BlockingIOError",          
    "ErroDeProcessoFilho":      "ChildProcessError",        #
    "ErroDeConexão":            "ConnectionError",
    "ErroDePipeQuebrado":       "BrokenPipeError",          
    "ErroDeConexãoAbortada":    "ConnectionAbortedError",
    "ErroDeConexãoRecusada":    "ConnectionRefusedError",
    "ErroDeConexãoRedefinida":  "ConnectionResetError",
    "ErroDeArquivoExistente":     "FileExistsError",
    "ErroDeArquivoNãoEncontrado": "FileNotFoundError",
    "ErroDeInterrupção":        "InterruptedError",
    "ErroÉUmDiretório":        "IsADirectoryError",
    "ErroNãoÉUmDiretório":     "NotADirectoryError",
    "ErroDePermissão":          "PermissionError",
    "ErroDeProcessoNãoEncontrado": "ProcessLookupError",
    "ErroDeTimeout":            "TimeoutError",
    # Warnings:
    "Aviso":                    "Warning",
    "AvisoDeUsuário":           "UserWarning",
    "AvisoDeDepreciação":       "DeprecationWarning",           #
    "AvisoDeDepreciaçãoPendente": "PendingDeprecatilonWarning",  #
    "AvisoDeSintaxe":           "SyntaxWarning",
    "AvisoDeExecução":          "RuntimeWarning",
    "AvisoFuturo":              "FutureWarning",
    "AvisoDeImportação":        "ImportWarning",
    "AvisoDeUnicode":           "UnicodeWarning",
    "AvisoDeCodificação":       "EncodingWarning",
    "AvisoDeBytes":             "BytesWarning",
    "AvisoDeRecurso":           "ResourceWarning",
    # Exception Groups:
    "GrupoDeExceções":          "ExceptionGroup",
    "GrupoDeExceçõesBase":      "BaseExceptionGroup",

}

traceback_dictionary = {
    "Traceback (most recent call last):": 
        "Traceback (chamada mais recente por último):",
    "line": 
        "linha",
    "File": 
        "Arquivo",
    "During handling of the above exception, another exception occurred":
        "Durante o tratamento da exceção acima, outra exceção ocorreu",
    "The above exception was the direct cause of the following exception":
        "A exceção acima foi a causa direta da seguinte exceção",
    "invalid syntax":
        "sintaxe inválida",
}
# traceback_dictionary = {v: k for k, v in inv_traceback_dictionary.items()}

# PYLYGLOT INTERNAL MESSAGES
# These are functions as the message may depend on specific information.
# A dictionary connecting keys to functions is defined at the end.
def pylyglot_version_warning(path, version, current_version):
    """f"Pylyglot file {path} generated with version {version}, but you are using {current_version} for translation! Translation could be inconsistent."""
    return f"O arquivo pylyglot {path} foi gerado com a versão {version}, mas a versão instalada é {current_version}! A tradução pode ser inconsistente."

inv_internal_pylyglot_dict = {
    "pylyglot_version_warning": pylyglot_version_warning
}
