dictionary = dict()
exception_dictionary = dict()
traceback_dictionary = dict()
pylyglot_internal_messages = dict()

dictionary = {
    # keyword.kwlist (from keyword import kwlist)
    # if/else    
    "se":         "if",
    "senãose":    "elif",
    "senão":      "else",
    # logic:
    "Caô":      "False",
    "Nada":     "None",       
    "Namoral": "True",
    "e":          "and",
    "ou":         "or",
    "nem":        "not",
    "é":          "is",
    "na":         "in",
    "ã":    "assert",     
    # Loops:
    "pracada":       "for",
    "enquanto":   "while",
    "bora":  "continue",
    "partiu":    "break",
    # try/except/finally
    "tenta":     "try",        
    "carai":     "except",     
    "fudeu":   "raise",      
    "finalmente": "finally",
    # imports
    "de":         "from",
    "chama":   "import",
    "quenem":       "as",
    # Functions/classes/generators
    "classe":     "class",
    "coé":        "def",        
    "fechô":   "return",     
    "lambda":     "lambda",
    "deu":   "yield",      
    # Others:
    "gringo":     "global",
    "paulista":   "nonlocal",
    "passa":     "pass",
    "asinc":    "async",    
    "pera":    "await",    
    "perdeu":        "del",
    "com":        "with",

    #builtins: https://docs.python.org/3/library/functions.html
    #A
    "abs":  "abs",
    "aiter":  "aiter", #
    "geral":  "all",
    "anext":  "anext",#
    "algum":  "any",
    "ascii":  "ascii",
    #B
    "bin": "bin",#
    "bool":         "bool",
    "breakpoint":         "breakpoint",#
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
    "frozenset":    "frozenset",#
    #G
    "buscaratr": "getattr",
    "gringos": "globals",
    #H
    "tematr": "hasattr",
    "hash": "hash",
    "nahumildade": "help",
    "hex": "hex",
    #I
    "id": "id",
    "input": "input",#
    "int":          "int",
    "étipo": "isinstance",
    "ésubclasse": "issubclass",
    "iter": "iter",#
    #L
    "tamanho": "len",
    "lista":        "list",
    "cariocas": "locals",
    #M
    "mapear": "map",
    "maior": "max",
    "memoryview": "memoryview",#
    "menó": "min",
    #N
    "próximo": "next",
    #O
    "objeto":       "object",
    "oct":       "oct",
    "abrir":       "open",
    "ord":       "ord",
    #P
    "pot":       "pow",
    "fala":   "print",
    "propriedade":   "property",
    #R
    "conta":    "range",
    "repr":    "repr",#
    "inverter":    "reversed",
    "arredondar":    "round",
    #S
    "conj":         "set",
    "defatr":          "setattr",
    "fatia":          "slice",
    "ordenar":          "sorted",
    "métodoestático":          "staticmethod",
    "str":          "str",
    "soma":          "sum",
    "opai":          "super",
    #T
    "tupla":         "tuple",
    "tipo":         "type",
    #V
    "vars": "vars",
    #Z
    "zip": "zip",

    #Others:
    "eu": "self",
    "__brota__": "__init__",
}