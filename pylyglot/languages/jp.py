# Japanese language pack for Pylyglot
# Notes on translation choices:
# - Keywords use romaji where Japanese programmers commonly use them (e.g. lambda, global)
# - Technical terms like "class", "def", "import" are kept in romaji as they are
#   universally used as-is in Japanese programming culture
# - Builtins are translated where a natural Japanese equivalent exists
# - Dunder methods use short romaji-based abbreviations following Japanese IT conventions

dictionary = {
    # Keywords
    "もし":         "if",
    "またもし":     "elif",
    "それ以外":     "else",
    # Logic
    "偽":           "False",
    "なし":         "None",
    "真":           "True",
    "かつ":         "and",
    "または":       "or",
    "でない":       "not",
    "です":         "is",
    "の中に":       "in",
    "確認":         "assert",
    # Loops
    "各々":         "for",
    "間":           "while",
    "続ける":       "continue",
    "やめる":       "break",
    # try/except/finally
    "試す":         "try",
    "除いて":       "except",
    "発生":         "raise",
    "最後に":       "finally",
    # Imports
    "から":         "from",
    "インポート":   "import",
    "として":       "as",
    # Functions/classes/generators
    "クラス":       "class",
    "定義":         "def",
    "返す":         "return",
    "lambda":       "lambda",   # lambda is used as-is in Japanese programming
    "生成":         "yield",
    # Others
    "グローバル":   "global",
    "非ローカル":   "nonlocal",
    "パス":         "pass",
    "非同期":       "async",
    "待つ":         "await",
    "削除":         "del",
    "と共に":       "with",

    # Builtins — many are kept in romaji as they are used directly in Japanese code
    "絶対値":       "abs",
    "aiter":        "aiter",    # technical, keep as-is
    "全て":         "all",
    "anext":        "anext",    # technical, keep as-is
    "どれか":       "any",
    "ascii":        "ascii",    # technical, keep as-is
    "二進":         "bin",
    "bool":         "bool",     # universally used as-is
    "ブレークポイント": "breakpoint",
    "バイト配列":   "bytearray",
    "バイト":       "bytes",
    "呼出可能":     "callable",
    "文字":         "chr",
    "クラスメソッド": "classmethod",
    "コンパイル":   "compile",
    "複素数":       "complex",
    "属性削除":     "delattr",
    "辞書":         "dict",
    "dir":          "dir",      # used as-is in Japanese
    "divmod":       "divmod",   # mathematical, keep as-is
    "列挙":         "enumerate",
    "評価":         "eval",
    "exec":         "exec",     # used as-is
    "フィルター":   "filter",
    "浮動小数":     "float",
    "format":       "format",   # used as-is in Japanese
    "凍結集合":     "frozenset",
    "属性取得":     "getattr",
    "グローバル変数":"globals",
    "属性確認":     "hasattr",
    "hash":         "hash",     # technical, keep as-is
    "ヘルプ":       "help",
    "hex":          "hex",      # mathematical, keep as-is
    "id":           "id",       # used as-is
    "入力":         "input",
    "int":          "int",      # universally used as-is
    "インスタンス確認": "isinstance",
    "サブクラス確認":  "issubclass",
    "iter":         "iter",     # technical, keep as-is
    "長さ":         "len",
    "リスト":       "list",
    "ローカル変数":  "locals",
    "マップ":       "map",
    "最大":         "max",
    "メモリビュー":  "memoryview",
    "最小":         "min",
    "次":           "next",
    "オブジェクト":  "object",
    "oct":          "oct",      # mathematical, keep as-is
    "開く":         "open",
    "ord":          "ord",      # mathematical, keep as-is
    "冪乗":         "pow",
    "表示":         "print",
    "プロパティ":   "property",
    "範囲":         "range",
    "repr":         "repr",     # technical, keep as-is
    "逆順":         "reversed",
    "丸め":         "round",
    "集合":         "set",
    "属性設定":     "setattr",
    "スライス":     "slice",
    "並べ替え":     "sorted",
    "静的メソッド": "staticmethod",
    "文字列":       "str",
    "合計":         "sum",
    "super":        "super",    # used as-is in Japanese OOP
    "タプル":       "tuple",
    "型":           "type",
    "vars":         "vars",     # technical, keep as-is
    "zip":          "zip",      # used as-is

    # Others
    "自身":         "self",
    "未実装":       "NotImplemented",

    # Dunder methods — using short recognizable forms
    "__初期化__":               "__init__",
    "__新規__":                 "__new__",
    "__削除__":                 "__del__",
    "__等価__":                 "__eq__",
    "__不等__":                 "__ne__",
    "__hash__":                 "__hash__",
    "__repr__":                 "__repr__",
    "__未満__":                 "__lt__",
    "__超過__":                 "__gt__",
    "__以下__":                 "__le__",
    "__以上__":                 "__ge__",
    "__文字列__":               "__str__",
    "__bool__":                 "__bool__",
    "__int__":                  "__int__",
    "__浮動__":                 "__float__",
    "__bytes__":                "__bytes__",
    "__複素__":                 "__complex__",
    "__format__":               "__format__",
    "__入室__":                 "__enter__",
    "__退室__":                 "__exit__",
    "__長さ__":                 "__len__",
    "__iter__":                 "__iter__",
    "__項目取得__":             "__getitem__",
    "__項目設定__":             "__setitem__",
    "__項目削除__":             "__delitem__",
    "__含む__":                 "__contains__",
    "__逆__":                   "__reversed__",
    "__次__":                   "__next__",
    "__欠落__":                 "__missing__",
    "__長さヒント__":           "__length_hint__",
    "__呼出__":                 "__call__",
    # Arithmetic
    "__加算__":                 "__add__",
    "__減算__":                 "__sub__",
    "__乗算__":                 "__mul__",
    "__除算__":                 "__truediv__",
    "__余剰__":                 "__mod__",
    "__整除__":                 "__floordiv__",
    "__冪__":                   "__pow__",
    "__行列乗__":               "__matmul__",
    "__論理積__":               "__and__",
    "__論理和__":               "__or__",
    "__排他和__":               "__xor__",
    "__右シフト__":             "__rshift__",
    "__左シフト__":             "__lshift__",
    # Right versions
    "__右加算__":               "__radd__",
    "__右減算__":               "__rsub__",
    "__右乗算__":               "__rmul__",
    "__右除算__":               "__rtruediv__",
    "__右余剰__":               "__rmod__",
    "__右整除__":               "__rfloordiv__",
    "__右冪__":                 "__rpow__",
    "__右行列乗__":             "__rmatmul__",
    "__右論理積__":             "__rand__",
    "__右論理和__":             "__ror__",
    "__右排他和__":             "__rxor__",
    "__右右シフト__":           "__rrshift__",
    "__右左シフト__":           "__rlshift__",
    # Inplace versions
    "__累加算__":               "__iadd__",
    "__累減算__":               "__isub__",
    "__累乗算__":               "__imul__",
    "__累除算__":               "__itruediv__",
    "__累余剰__":               "__imod__",
    "__累整除__":               "__ifloordiv__",
    "__累冪__":                 "__ipow__",
    "__累行列乗__":             "__imatmul__",
    "__累論理積__":             "__iand__",
    "__累論理和__":             "__ior__",
    "__累排他和__":             "__ixor__",
    "__累右シフト__":           "__irshift__",
    # Unary
    "__負__":                   "__neg__",
    "__正__":                   "__pos__",
    "__反転__":                 "__invert__",
    # Math builtins
    "__除余__":                 "__divmod__",
    "__右除余__":               "__rdivmod__",
    "__絶対__":                 "__abs__",
    "__索引__":                 "__index__",
    "__丸め__":                 "__round__",
    "__切捨__":                 "__trunc__",
    "__床__":                   "__floor__",
    "__天井__":                 "__ceil__",
    # Attributes
    "__属性取得__":             "__getattr__",
    "__属性取得詳__":           "__getattribute__",
    "__属性設定__":             "__setattr__",
    "__属性削除__":             "__delattr__",
    "__dir__":                  "__dir__",
    # Metaprogramming
    "__準備__":                 "__prepare__",
    "__インスタンス確認__":     "__instancecheck__",
    "__サブクラス確認__":       "__subclasscheck__",
    "__サブクラス初期化__":     "__init_subclass__",
    "__サブクラス群__":         "__subclasses__",
    "__mro項目__":              "__mro_entries__",
    "__クラス項目__":           "__class_getitem__",
    # Descriptors
    "__名前設定__":             "__set_name__",
    "__取得__":                 "__get__",
    "__設定__":                 "__set__",
    "__消去__":                 "__delete__",
    # Buffers
    "__バッファ__":             "__buffer__",
    "__バッファ解放__":         "__release_buffer__",
    # Async
    "__非同期入室__":           "__aenter__",
    "__非同期退室__":           "__aexit__",
    "__aiter__":                "__aiter__",
    "__非同期次__":             "__anext__",
    "__待機__":                 "__await__",
    # Library-specific
    "__post_init__":            "__post_init__",
    "__サブクラスフック__":     "__subclasshook__",
    "__ファイルパス__":         "__fspath__",
    "__複写__":                 "__copy__",
    "__深複写__":               "__deepcopy__",
    "__置換__":                 "__replace__",
    "__新引数取得拡__":         "__getnewargs_ex__",
    "__新引数取得__":           "__getnewargs__",
    "__状態取得__":             "__getstate__",
    "__状態設定__":             "__setstate__",
    "__縮小__":                 "__reduce__",
    "__縮小拡__":               "__reduce_ex__",
    "__サイズ__":               "__sizeof__",

    # Dunder attributes
    "__名前__":                 "__name__",
    "__モジュール__":           "__module__",
    "__doc__":                  "__doc__",
    "__クラス__":               "__class__",
    "__辞書__":                 "__dict__",
    "__slots__":                "__slots__",
    "__match_args__":           "__match_args__",
    "__mro__":                  "__mro__",
    "__基底__":                 "__bases__",
    "__ファイル__":             "__file__",
    "__wrapped__":              "__wrapped__",
    "__バージョン__":           "__version__",
    "__全て__":                 "__all__",
    "__debug__":                "__debug__",
    "__既定値__":               "__defaults__",
    "__kw既定値__":             "__kwdefaults__",
    "__コード__":               "__code__",
    "__グローバル__":           "__globals__",
    "__クロージャ__":           "__closure__",
    "__修飾名__":               "__qualname__",
    "__注釈__":                 "__annotations__",
    "__型パラメータ__":         "__type_params__",
    "__静的属性__":             "__static_attributes__",
    "__初行番号__":             "__firstlineno__",
    "__関数__":                 "__func__",
    "__自身__":                 "__self__",
    "__ローダー__":             "__loader__",
    "__パッケージ__":           "__package__",
    "__spec__":                 "__spec__",
    "__cached__":               "__cached__",
    "__パス__":                 "__path__",
    "__traceback__":            "__traceback__",
    "__注記__":                 "__notes__",
    "__コンテキスト__":         "__context__",
    "__原因__":                 "__cause__",
    "__コンテキスト抑制__":     "__suppress_context__",
    "__objclass__":             "__objclass__",
    "__classcell__":            "__classcell__",
    "__弱参照__":               "__weakref__",
    "__起源__":                 "__origin__",
    "__args__":                 "__args__",
    "__パラメータ__":           "__parameters__",
    "__unpacked__":             "__unpacked__",
    "__標準出力__":             "__stdout__",
    "__標準エラー__":           "__stderr__",
    "__共変__":                 "__covariant__",
    "__反変__":                 "__contravariant__",
    "__分散推論__":             "__infer_variance__",
    "__境界__":                 "__bound__",
    "__制約__":                 "__constraints__",
    "__インポート__":           "__import__",
    "__builtins__":             "__builtins__",
    "__future__":               "__future__",
    "__main__":                 "__main__",
}

exception_dictionary = {
    "基底例外":                 "BaseException",
    "例外":                     "Exception",
    "算術エラー":               "ArithmeticError",
    "バッファエラー":           "BufferError",
    "検索エラー":               "LookupError",
    "表明エラー":               "AssertionError",
    "属性エラー":               "AttributeError",
    "ファイル終端エラー":       "EOFError",
    "浮動小数点エラー":         "FloatingPointError",
    "ジェネレータ終了":         "GeneratorExit",
    "インポートエラー":         "ImportError",
    "モジュール未発見エラー":   "ModuleNotFoundError",
    "インデックスエラー":       "IndexError",
    "キーエラー":               "KeyError",
    "キーボード割り込み":       "KeyboardInterrupt",
    "メモリエラー":             "MemoryError",
    "名前エラー":               "NameError",
    "未実装エラー":             "NotImplementedError",
    "OSエラー":                 "OSError",
    "オーバーフローエラー":     "OverflowError",
    "Python終了エラー":         "PythonFinalizationError",
    "再帰エラー":               "RecursionError",
    "参照エラー":               "ReferenceError",
    "実行時エラー":             "RuntimeError",
    "反復停止":                 "StopIteration",
    "非同期反復停止":           "StopAsyncIteration",
    "構文エラー":               "SyntaxError",
    "字下げエラー":             "IndentationError",
    "タブエラー":               "TabError",
    "システムエラー":           "SystemError",
    "システム終了":             "SystemExit",
    "型エラー":                 "TypeError",
    "未束縛変数エラー":         "UnboundLocalError",
    "Unicodeエラー":            "UnicodeError",
    "Unicode符号化エラー":      "UnicodeEncodeError",
    "Unicode復号エラー":        "UnicodeDecodeError",
    "Unicode変換エラー":        "UnicodeTranslateError",
    "値エラー":                 "ValueError",
    "ゼロ除算エラー":           "ZeroDivisionError",
    "環境エラー":               "EnvironmentError",
    "IOエラー":                 "IOError",
    "Windowsエラー":            "WindowsError",
    "ブロッキングIOエラー":     "BlockingIOError",
    "子プロセスエラー":         "ChildProcessError",
    "接続エラー":               "ConnectionError",
    "パイプ切断エラー":         "BrokenPipeError",
    "接続中断エラー":           "ConnectionAbortedError",
    "接続拒否エラー":           "ConnectionRefusedError",
    "接続リセットエラー":       "ConnectionResetError",
    "ファイル存在エラー":       "FileExistsError",
    "ファイル未発見エラー":     "FileNotFoundError",
    "割り込みエラー":           "InterruptedError",
    "ディレクトリエラー":       "IsADirectoryError",
    "非ディレクトリエラー":     "NotADirectoryError",
    "権限エラー":               "PermissionError",
    "プロセス未発見エラー":     "ProcessLookupError",
    "タイムアウトエラー":       "TimeoutError",
    "警告":                     "Warning",
    "ユーザー警告":             "UserWarning",
    "非推奨警告":               "DeprecationWarning",
    "保留非推奨警告":           "PendingDeprecationWarning",
    "構文警告":                 "SyntaxWarning",
    "実行時警告":               "RuntimeWarning",
    "将来警告":                 "FutureWarning",
    "インポート警告":           "ImportWarning",
    "Unicode警告":              "UnicodeWarning",
    "符号化警告":               "EncodingWarning",
    "バイト警告":               "BytesWarning",
    "リソース警告":             "ResourceWarning",
    "例外グループ":             "ExceptionGroup",
    "基底例外グループ":         "BaseExceptionGroup",
}

traceback_dictionary = {
    "Traceback (most recent call last):":
        "トレースバック（直近の呼び出しが最後）:",
    "line":     "行",
    "File":     "ファイル",
    "During handling of the above exception, another exception occurred":
        "上記の例外を処理中に、別の例外が発生しました",
    "The above exception was the direct cause of the following exception":
        "上記の例外が以下の例外の直接の原因です",
    "invalid syntax":
        "構文が無効です",
}

pylyglot_internal_messages = {
    "main_arg_length_error":
        "Pylyglotは少なくとも1つのオプション（ファイルパス）を受け取る必要があります。",
    "main_file_specified_twice":
        "ファイルパスが2回指定されました？{filepath}、{arg}。",
    "main_couldnt_interpret_argument":
        "引数を解釈できませんでした: {arg}。正しいパスを指定してください。",
    "main_couldnt_find_filepath":
        "コマンドライン引数からファイルパスを識別できませんでした。",
    "main_console_and_translate":
        '"console"と"translate"オプションが同時に指定されました（一方のみ許可）。',
    "main_translate_destination":
        "--translateオプションには出力先が必要です: python -m pylyglot --translate=output_language source_path destination_path",
    "main_no_output_language_verbose":
        "翻訳言語が指定されていません。拡張子から識別された言語: {lang}。",
    "main_defaulting_to_default_language":
        "言語が指定されていないため、デフォルト言語に翻訳します: {default_language}。"
        '\nデフォルト言語は次のコマンドで変更できます: "python -m pylyglot --setconfig default_language=言語コード"。',
    "main_file_and_destination_type_mismatch":
        "指定されたパス ({filepath}) はディレクトリですが、出力先はディレクトリではありません ({destination})。",
    "main_console_language":
        "Pylyglot警告: コンソールの言語が指定されていないため、デフォルト言語を使用します: {default_language}。"
        '\nデフォルト言語は次のコマンドで変更できます: "python -m pylyglot --setconfig default_language=言語コード"。',
    "config_key_error":
        '"{key}"はPylyglot設定に存在しません。'
        '\nオプションを確認するには: "python -m pylyglot --getconfig"'
        '\n設定ファイルのパスを確認するには: "python -m pylyglot --getconfigpath"',
    "config_set_success":
        '設定オプション"{key}"を"{old_value}"から"{value}"に更新しました。',
    "config_reset_success":
        "設定がデフォルト値にリセットされました。",
    "config_allow_renames":
        '"allow_renames"オプションのデフォルト値を設定することは許可されていません。',
    "translator_version_warning":
        "pylyglotファイル{path}はバージョン{version}で生成されましたが、{current_version}を使用して翻訳しています。翻訳が不整合になる可能性があります。",
    "translator_language_id_fail":
        "ファイルの言語を識別できませんでした: {path}",
    "translator_syntaxerror":
        "Pylyglot警告: 構文エラーは英語のPythonキーワードの使用に起因する可能性があります。\n",
    "translator_rename_dict":
        "翻訳対象ファイル({path})には、出力言語に存在する以下の語が含まれています: {rename_keys}。"
        "\nPylyglotはこれらの変数を自動的に名前変更できますが、セキュリティリスクが生じる可能性があります。"
        "\n手動での変数名変更を強くお勧めします。"
        "\nリスクを承知で続行するには --allow_renames=true を使用してください。",
    "hooks_duplicate_module":
        'モジュール"{fullname}"のインポート中にエラーが発生しました: 同じ名前のモジュールが複数見つかりました ({dir_path}): {potential_files}。',
}

dictionary.update(exception_dictionary)
traceback_dictionary.update({v: k for k, v in exception_dictionary.items()})