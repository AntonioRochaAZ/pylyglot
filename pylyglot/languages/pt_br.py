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
    "gerar":      "yield",      
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
    "aiter":  "aiter",
    "todos":  "all",
    "apróx":  "anext",
    "algum":  "any",
    "ascii":  "ascii",
    #B
    "bin": "bin",
    "bool":         "bool",
    "pontodeparada":         "breakpoint",
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
    "dir":        "dir",
    "divres": "divmod",
    #E
    "enumerar": "enumerate",
    "aval": "eval",
    "exec": "exec",
    #F
    "filtrar":  "filter",
    "flut":     "float",
    "format":   "format",
    "conjfixo": "frozenset",
    #G
    "buscatr":  "getattr",
    "globais":  "globals",
    #H
    "tematr":   "hasattr",
    "hash":     "hash",
    "ajuda":    "help",
    "hex":      "hex",
    #I
    "id":       "id",
    "entrada":  "input",
    "int":      "int",
    "éinstância":   "isinstance",
    "ésubclasse":   "issubclass",
    "iter":     "iter",
    #L
    "tamanho":  "len",
    "lista":    "list",
    "locais":   "locals",
    #M
    "mapear":   "map",
    "max":      "max",
    "vismemória":   "memoryview",
    "min":      "min",
    #N
    "próximo":  "next",
    #O
    "objeto":   "object",
    "oct":      "oct",
    "abrir":    "open",
    "ord":      "ord",
    #P
    "pot":      "pow",
    "imprimir": "print",
    "propriedade":  "property",
    #R
    "intervalo":    "range",
    "repr":     "repr",     #
    "inverter": "reversed",
    "arred":    "round",
    #S
    "conj":     "set",
    "defatr":   "setattr",
    "fatia":    "slice",
    "ordenar":  "sorted",
    "métodoestático":   "staticmethod",
    "txt":      "str",
    "soma":     "sum",
    "super":    "super",
    #T
    "tupla":    "tuple",
    "tipo":     "type",
    #V
    "vars":     "vars",
    #Z
    "zip":      "zip",

    #Others:
    "si":       "self",

    #Other builtins
    "NãoImplementado": "NotImplemented",
 
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
    "__divresdir__":            "__rdivmod__",
    "__abs__":                  "__abs__",
    "__índice__":               "__index__",
    "__arred__":                "__round__",
    "__trunc__":                "__trunc__",
    "__chão__":                 "__floor__",
    "__teto__":                 "__ceil__",
    # Attribute
    "__buscatr__":              "__getattr__",
    "__buscatributo__":         "__getattribute__",
    "__defatr__":               "__setattr__",
    "__delatr__":               "__delattr__",
    "__dir__":                  "__dir__",

    # Metaprogramming:
    "__preparar_":              "__prepare__",
    "__veriféinstância__":      "__instancecheck__",
    "__verifésubclasse__":      "__subclasscheck__",
    "__inic_subclasse__":       "__init_subclass__",
    "__subclasses__":           "__subclasses__",
    "__entidades_orm__":        "__mro_entries__",
    "__buscaritem_classe__":    "__class_getitem__",

    # Descriptors:
    "__def_nome__":             "__set_name__",
    "__buscar__":               "__get__",
    "__def__":                  "__set__",
    "__deletar__":              "__delete__",

    # Buffers:
    "__buffer__":               "__buffer__",
    "__liberar_buffer__":       "__release_buffer__",

    # Asynchronous operations:
    "__aentrar__":              "__aenter_",
    "__asair__":                "__aexit__",
    "__aiter__":                "__aiter__",
    "__apróx__":                "__anext__",
    "__esperar__":              "__await__",

    # Library-specific
    "__pós_inic__":             "__post_init__",
    "__ganchosubclasse__":      "__subclasshook__",
    # "": "__subclasscheck__", # Defined earlier
    "__fscaminho__":            "__fspath__",
    "__copiar__":               "__copy__",
    "__cópiaprofunda__":        "__deepcopy__",
    "__substit__":              "__replace__",
    "__buscarnovargs_ex__":     "__getnewargs_ex__",
    "__buscarnovargs__":        "__getnewargs__",
    "__buscarestado__":         "__getstate__",
    "__defestado__":            "__setstate__",
    "__reduzir__":              "__reduce__",
    "__reduzir_ex__":           "__reduce_ex__",
    "__tamanhode__":            "__sizeof__",


    # Dunder attributes/constants: https://www.pythonmorsels.com/every-dunder-method/
    "__nome__":     "__name__",
    "__módulo__":   "__module__",
    "__doc__":      "__doc__",
    "__classe__":   "__class__",
    "__dicio__":    "__dict__",
    "__slots__":    "__slots__",               # TODO
    "__match_args__":   "__match_args__",     # TODO

    "__orm__":      "__mro__", # Method Resolution Order
    "__bases__":    "__bases__",
    "__arquivo__":  "__file__",
    "__embrulhados__":  "__wrapped__",

    "__versão__":   "__version__",
    "__todos__":    "__all__",
    "__debug__":    "__debug__",

    "__padrões__":      "__defaults__",
    "__padrõeskw__":    "__kwdefaults__",
    "__código__":       "__code__",
    "__globais__":      "__globals__",
    "__fechamento__":   "__closure__",
    
    # "": "__qualname__",
    # "": "__annotations__",
    # "": "__type_params__",

    # "": "__static_attributes__",
    # "": "__firstlineno__",

    # "": "__func__",
    # "": "__self__",

    # "": "__loader__",
    # "": "__package__",
    # "": "__spec__",
    # "": "__cached__",

    "__caminho__":      "__path__",

    # "": "__traceback__",
    # "": "__notes__",
    # "": "__context__",
    # "": "__cause__",
    # "": "__suppress_context__",

    # "": "__objclass__",
    # "": "__classcell__",
    # "": "__weakref__",

    # "": "__origin__",
    # "": "__args__",
    # "": "__parameters__",
    # "": "__unpacked__",

    # "": "__stdout__",
    # "": "__stderr__",

    # "": "__covariant__",
    # "": "__contravariant__",
    # "": "__infer_variance__",
    # "": "__bound__",
    # "": "__constraints__",
    # "": "__import__",
    # "": "__builtins__",
    "__futuro__":   "__future__",
    "__main__":     "__main__",

}

exception_dictionary = {
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
    "ErroDeSO":                 "OSError",                  
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
    "ErroDeProcessoFilho":      "ChildProcessError",        
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
    "AvisoDeObsolescência":         "DeprecationWarning",          
    "AvisoDeObsolescênciaPendente": "PendingDeprecatilonWarning", 
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


# traceback_dict: English --> Your language
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


# PYLYGLOT INTERNAL MESSAGES
pylyglot_internal_messages = {
    # __main__.py :
    "main_arg_length_error": 
        # "Pylyglot must receive at least 1 options: the path to the file.",
        "Pylyglot precisa de ao menos uma opção: o caminho do arquivo.",
    "main_file_specified_twice": 
        # "File path specified twice? {filepath}, {arg}.",
        "Caminho de arquivo especificado duas vezes? {filepath}, {arg}.",
    "main_couldnt_interpret_argument": 
        # "Couldn't interpret argument: {arg}. Make sure you have provided the right paths.",
        "Impossível interpretar argumento: {arg}. Certifique-se de especificar os caminhos corretamente.",
    "main_couldnt_find_filepath": 
        # "Could not identify filepath in command line arguments.",
        "Não foi possível identificar o caminho do arquivo à partir dos argumentos.",
    "main_console_and_translate": 
        # 'Pylyglot received both "console" and "translate" options at the same time (only one allowed).',
        'Pylyglot recebeu as opções "console" e "translate" ao mesmo tempo (apenas uma permitida).',
    "main_translate_destination": 
        # "--translate requires a destination: python -m pylyglot --translate=output_language source_path destination_path", 
        "A opção --translate requer um caminho de destino: python -m pylyglot --translate=output_language source_path destination_path", 
    "main_no_output_language_verbose": 
        # 'No translation language was specified for the translate option. Language identified by the destination file extension: {lang}.',
        'A língua de tradução não foi especificada pela opção "translate". Língua identificada pela extensão do arquivo de destino: {lang}.',
    "main_defaulting_to_default_language": 
        # 'No translation language was specified for the translate option, translating to default language: {default_language}.'
        # '\nYou can change the default language by running "python -m pylyglot --setconfig default_langauge=language_code".',
        'Nenhuma língua foi especificada pela opção "translate", traduzindo para a língua padrão: {default_language}.'
        '\nVocê pode alterar a língua padrão rodando: "python -m pylyglot --setconfig default_langauge=language_code".',
    "main_file_and_destination_type_mismatch":
        # "Specified filepath for translation ({filepath}) is a directory, but destination isn't ({destination}).",
        "Caminho especificado para trandução ({filepath}) é um diretório, mas a desinação não ({destination}).",
    "main_console_language":
        # 'Pylyglot warning: No console language specified, using default langauge: {default_language}.'
        # '\nYou can change the default language by running "python -m pylyglot --setconfig default_langauge=language_code".',
        'Aviso Pylyglot: Nenhuma língua especificada para a console, usando língua padrão: {default_language}.'
        '\nVocê pode alterar a língua padrão rodando: "python -m pylyglot --setconfig default_langauge=language_code".',
    
    # config.py:
    "config_key_error":
        # '"{key}" not in pylyglot config file.'
        # '\nTo see options, run "python -m pylyglot --getconfig"'
        # '\nTo get the path to the config.json, run "python -m pylyglot --getconfigpath"',
        'A opção "{key}" não faz partes das configurações pylyglot.'
        '\nPara ver as opções disponíveis, rodar: "python -m pylyglot --getconfig"'
        '\nPara o caminho até o arquivo de configuração config.json, rodar: "python -m pylyglot --getconfigpath"',
    "config_set_success":
        # 'Successfully updated config option "{key}" from "{old_value}" to "{value}".',
        'Opção de configuração "{key}" atualizada com sucesso de "{old_value}" para "{value}".',
    "config_reset_success":
        # "Config was reset to defaults.",
        "As configurações foram re-ininicializadas para os valores padrões. Para vê-los, lance: python -m pylyglot --getconfig",
    "config_allow_renames":
        # 'It is not allowed to set a default value for the "allow_renames" option.',
        'Não é permitido definir um valor padrão para a opção "allow_renames".',
    
    # translator.py:
    "translator_version_warning": 
        # "Pylyglot file {path} generated with version {version}, but you are using {current_version} for translation! Translation could be inconsistent.",
        "O arquivo pylyglot {path} foi gerado com a versão {version}, mas você está usando a versão {current_version} para tradução! A tradução pode ser inconsistente.",
    "translator_language_id_fail":
        # "Could not identify language of the following file: {path}",
        "Impossível de identificar a língua do arquivo: {path}",
    "translator_syntaxerror":
        # "Pylyglot Warning: SyntaxErrors may come from the use of python keywords in code.\n",
        "Aviso pylyglot: ErroDeSintaxe pode vir do uso de termos python (em inglês) em seu código.\n",
    "translator_rename_dict":
        # "File being translated ({path}) contains the following words present in the destination language: {rename_keys}."
        # "\nPylyglot is able to automatically rename these variables and run the file, but this may not cause the desired behaviour "
        # "and THIS MAY EXPOSE YOU TO SECURITY RISKS."
        # "\nModules imported by this module may suffer from the same issue and not have been reported in this message."
        # "\nFor these reasons, it is highly recommended that the user rename these variables manually."
        # "\nTo allow pylyglot to run the file and its imports regardless, you can pass the option --allow_renames=true (this option cannot be "
        # "set to the config and must be specified for every new run).",
        "O arquivo a ser traduzido ({path}) contém as seguintes palavras, presente na língua de destino: {rename_keys}."
        "\nO pylyglot é capaz de automaticamente renomear essas variáveis, e rodar o arquivo, mas isto pode não causar o comportamento esperado, "
        "além de POTENCIALMENTE EXPÔR O USUÁRIO A RISCOS DE SEGURANÇA."
        "\nMódulos importados por este módulo também podem ter o mesmo problema, e não terem sido relatados nesta mensagem."
        "\nPor esses motivos, é extremamente recomendado que o usuário renomeie manualmente as variávies citadas."
        "\nPara aceitar o risco e permitir que pylyglot rode o arquivo et suas importações de toda forma apenas com um aviso, você pode passar a opção --allow_renames=true "
        "(essa opção não pode ser integrada às configurações, e deve ser especificada a cada vez).",

    # hooks.py:
    "hooks_duplicate_module":
        # 'Error when trying to import module "{fullname}": Multiple modules with the same name in the same directory ({dir_path}): {potential_files}',
        'Erro ao tentar importar o módulo "{fullname}": Múltiplos módulos com o mesmo nome no diretório ({dir_path}): {potential_files}.',


}

dictionary.update(exception_dictionary)
traceback_dictionary.update({v: k for k, v in exception_dictionary.items()})
