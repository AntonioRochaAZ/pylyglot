traceback_dictionary = dict()
pylyglot_internal_messages = dict()

# Disclaimer: made by ChatGPT
dictionary = {
    # if/else    
    "条件分岐":     "if",
    "追加条件":     "elif",
    "その他":       "else",

    # logic:
    "偽値":         "False",
    "無値":         "None",       
    "真値":         "True",
    "論理積":       "and",
    "論理和":       "or",
    "否定":         "not",
    "同一性":       "is",
    "所属":         "in",
    "検証":         "assert",

    # Loops:
    "反復":         "for",
    "条件反復":     "while",
    "反復継続":     "continue",
    "反復終了":     "break",

    # try/except/finally
    "試行":         "try",        
    "例外処理":     "except",     
    "例外送出":     "raise",      
    "最終処理":     "finally",

    # imports
    "元指定":       "from",
    "読込":         "import",
    "別名":         "as",

    # Functions/classes/generators
    "クラス":       "class",
    "関数定義":     "def",        
    "返却":         "return",     
    "ラムダ式":     "lambda",
    "生成":         "yield",      

    # Others:
    "大域":         "global",
    "非局所":       "nonlocal",
    "空処理":       "pass",
    "非同期":       "async",    
    "待機":         "await",    
    "削除":         "del",
    "文脈管理":     "with",

    # builtins
    # A
    "絶対値":       "abs",
    "非同期反復子": "aiter",
    "全要素":       "all",
    "非同期次要素": "anext",
    "任意要素":     "any",
    "ASCII変換":    "ascii",

    # B
    "二進変換":     "bin",
    "論理型":       "bool",
    "停止点":       "breakpoint",
    "バイト配列":   "bytearray",
    "バイト列":     "bytes",

    # C
    "呼出可能":     "callable",
    "文字変換":     "chr",
    "クラスメソッド": "classmethod",
    "コンパイル":   "compile",
    "複素数型":     "complex",

    # D
    "属性削除":     "delattr",
    "辞書型":       "dict",
    "一覧取得":     "dir",
    "除算剰余":     "divmod",

    # E
    "列挙":         "enumerate",
    "評価":         "eval",
    "実行":         "exec",

    # F
    "フィルタ処理": "filter",
    "浮動小数点":   "float",
    "書式化":       "format",
    "凍結集合":     "frozenset",

    # G
    "属性取得":     "getattr",
    "大域一覧":     "globals",

    # H
    "属性存在確認": "hasattr",
    "ハッシュ値":   "hash",
    "支援":         "help",
    "十六進変換":   "hex",

    # I
    "識別子":       "id",
    "入力":         "input",
    "整数型":       "int",
    "インスタンス判定": "isinstance",
    "部分型判定":   "issubclass",
    "反復子":       "iter",

    # L
    "長さ":         "len",
    "リスト型":     "list",
    "局所一覧":     "locals",

    # M
    "写像":         "map",
    "最大値":       "max",
    "メモリビュー": "memoryview",
    "最小値":       "min",

    # N
    "次要素":       "next",

    # O
    "オブジェクト": "object",
    "八進変換":     "oct",
    "開く":         "open",
    "順序値":       "ord",

    # P
    "累乗":         "pow",
    "出力":         "print",
    "属性定義":     "property",

    # R
    "範囲":         "range",
    "表現":         "repr",
    "逆順":         "reversed",
    "丸め":         "round",

    # S
    "集合型":       "set",
    "属性設定":     "setattr",
    "部分列":       "slice",
    "整列":         "sorted",
    "静的メソッド": "staticmethod",
    "文字列型":     "str",
    "総和":         "sum",
    "上位参照":     "super",

    # T
    "タプル型":     "tuple",
    "型":           "type",

    # V
    "変数一覧":     "vars",

    # Z
    "結合":         "zip",

    # Others:
    "自己参照":     "self",
    "__初期化__":   "__init__",
}

exception_dictionary = {
    "値エラー": "ValueError"
}

dictionary = dictionary | exception_dictionary
