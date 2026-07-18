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
    "paracada":       "for",
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
    "função":        "def",        
    "retornar":   "return",     
    "lambda":     "lambda",
    "gerar":   "yield",      
    # Others:
    "global":     "global",
    "nãolocal":   "nonlocal",
    "passar":     "pass",
    "asíncrona":    "async",    
    "esperar":    "await",    
    "deletar":        "del",
    "com":        "with",

    #builtins: https://docs.python.org/3/library/functions.html
    #A
    "absoluto":  "abs",
    "aiter":  "aiter", #
    "todos":  "all",
    "anext":  "anext",#
    "algum":  "any",
    "ascii":  "ascii",
    #B
    "bin": "bin",#
    "booleana":         "bool",
    "breakpoint":         "breakpoint",#
    "matrizbytes":  "bytearray",
    "bytes":        "bytes",
    #C
    "chamável":    "callable",
    "caracter":    "chr",
    "métododeclasse":    "classmethod",
    "compilar":    "compile",
    "complexo":     "complex",
    #D
    "deletaratributo": "delattr",
    "dicionário":        "dict",
    "dir":        "dir",#
    "divmod": "divmod",#
    #E
    "enumerar": "enumerate",
    "avaliar": "eval",
    "executar": "exec",
    #F
    "filtrar": "filter",
    "real":    "float",
    "format":  "format",
    "frozenset":    "frozenset",#
    #G
    "buscaratributo": "getattr",
    "globais": "globals",
    #H
    "tematributo": "hasattr",
    "hash": "hash",
    "ajuda": "help",
    "hexadecimal": "hex",
    #I
    "identidade": "id",
    "input": "input",#
    "inteiro":          "int",
    "éinstância": "isinstance",
    "ésubclasse": "issubclass",
    "iter": "iter",#
    #L
    "tamanho": "len",
    "lista":        "list",
    "locais": "locals",
    #M
    "mapear": "map",
    "máximo": "max",
    "memoryview": "memoryview",#
    "mínimo": "min",
    #N
    "próximo": "next",
    #O
    "objeto":       "object",
    "oct":       "oct",
    "abrir":       "open",
    "ord":       "ord",
    #P
    "potência":       "pow",
    "imprimir":   "print",
    "propriedade":   "property",
    #R
    "intervalo":    "range",
    "repr":    "repr",#
    "inverter":    "reversed",
    "arredondar":    "round",
    #S
    "conjunto":         "set",
    "definiratributo":          "setattr",
    "fatia":          "slice",
    "ordenar":          "sorted",
    "métodoestático":          "staticmethod",
    "string":          "str",
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
    "__inicializar__": "__init__",
}