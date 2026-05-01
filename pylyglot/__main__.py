if __name__ == "__main__":

    import sys
    import os
    from .translator import get_dictionary, run_file
    from .hooks import install
    install()

    args = sys.argv

    # pylyglot pt_br file_path --> python pylyglot_main.py pt_br file_path
    # -> args: pylyglot_main.py pt_br file_path

    if len(args) < 2:
        raise SyntaxError("pylyglot must receive at least 1 options: the path to the file.")
    
    # Ignore current file name:
    args = args[1:]

    language = None
    filepath = None
    options  = dict()
    for arg in args:
        if arg.startswith("--"): # option
            if "=" not in arg:
                raise SyntaxError(f'Option {arg} specified incorrectly, use the syntax: "--option=value".')
            option, value = arg.split("=")
            options[option] = value
        elif os.path.exists(arg):
            if filepath is not None:
                raise SyntaxError(f"File path specified twice? {filepath}, {arg}.")
            filepath = os.path.abspath(arg)
        else:
            # Check if it is a language:
            d = get_dictionary(arg, throw_exception=False)
            if d is not None:
                if language is not None:
                    raise SyntaxError(f"Language specified twice? {language}, {arg}.")
                language = arg
            else:
                raise SyntaxError(f"Couldn't interpret argument: {arg}")
    
    if filepath is None:
        raise SyntaxError("Could not identify filepath in command line arguments.")

    run_file(filepath, language, **options)