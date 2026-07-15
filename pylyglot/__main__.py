if __name__ == "__main__":
    import sys, os, re
    from warnings import warn

    from .hooks import install
    from .translator import translate_and_write, run_file 
    from .console import launch_console
    
    # Install hooks to allow imports from other languages:
    install()

    args = sys.argv

    if len(args) < 2:
        raise SyntaxError("pylyglot must receive at least 1 options: the path to the file.") # TODO: convert this to a language dependent thing.
    
    # Ignore current file name:
    args = args[1:]
    
    # Getting options:
    filepath = None
    options  = {"verbose": False, "encoding": "utf-8", "errors": "strict", "output-encoding": "utf-8"}  # default values
    """
    We also have two mutually exclusive options:
    --translate=<output_language>
    --console=<console_input_language>
    """
    for arg in args:
        if arg.startswith("--"): # option
            if "=" not in arg:
                options[arg.removeprefix("--")] = None
            else:
                option, value = arg.split("=")
                options[option.removeprefix("--")] = value
        elif os.path.exists(arg) or ("translate" in options and filepath is not None):
            # In the first case, we have either the source or an already existing destination file.
            # In the second case, we have the --translate and the potential of a destination file which does not already exist 
            if filepath is not None and "translate" not in options:
                # os.path.exists(arg) was triggered but --translate not in options
                raise SyntaxError(f"File path specified twice? {filepath}, {arg}.") # TODO: convert this to a language dependent thing.
            if filepath is None:
                # First time we find an existing file path, must be the source file
                filepath = os.path.abspath(arg)
            else:
                # We found the translation destination file:
                options["__destination__"] = os.path.abspath(arg)
        else:
            raise SyntaxError(f"Couldn't interpret argument: {arg}. Make sure you have provided the right paths.") # TODO: convert this to a language dependent thing.
    
    # Handling unexpected options:
    if filepath is None and "console" not in options:
        raise SyntaxError("Could not identify filepath in command line arguments.") # TODO: convert this to a language dependent thing.

    if "console" in options and "translate" in options:
        raise ValueError('pylyglot received both "console" and "translate" options at the same time (only one allowed).') # TODO: convert this to a language dependent thing.

    # Handle --translate option:
    if "translate" in options:
        output_language = options.pop("translate")
        if output_language is None: # Happens if the user just passes "--translate"
            output_language = "en"
            if options.get("verbose", "false").lower() == "true":
                warn('No output language was specified for the translate option, translating to regular Python.') # TODO: convert this to a language dependent thing.

        if str(output_language).lower() == "none": output_language = "en"
        destination = options.pop("__destination__", None)
        if destination is None:
            raise SyntaxError("--translate requires a destination: python -m pylyglot --translate=output_language source_path destination_path") # TODO: convert this to a language dependent thing.

        if os.path.isdir(filepath):
            if os.path.exists(destination):
                if not os.path.isdir(destination):
                    raise ValueError(f"Specified filepath for translation ({filepath}) is a directory, but destination isn't ({destination}).") # TODO: convert this to a language dependent thing.
            # If the input is a folder:
            # Walk through the folders and convert all .py files into our output language:
            for root, dirs, files in os.walk(filepath):
                for filename in files:
                    if not filename.endswith(".py"):
                        continue
                    src_path = os.path.join(root, filename)
                    relative = os.path.relpath(src_path, filepath)
                    
                    # swap .py with .{language}.py in the relative path
                    if output_language is not None:
                        relative_translated = re.sub(r"(\.[a-z_]*)?\.py$", f'.{output_language}.py', relative)
                    else:
                        relative_translated = re.sub(r"(\.[a-z_]*)?\.py$", f'.py', relative)
                    # Create destination path:                    
                    dst_path = os.path.join(destination, relative_translated)
                    # Translate and write:
                    translate_and_write(src_path, dst_path, output_language, **options)
        else:
            # Input is NOT a folder
            # if destination doesn't already have the language extension, add it
            if output_language != "en":
                if not destination.endswith(f'.{output_language}.py'):
                    base = re.sub(r"(\.[a-z_]*)?\.py$", '', destination) # Eventually correcting the extension
                    destination = f'{base}.{output_language}.py'
            else:
                if not destination.endswith(f'.py'):
                    destination = destination+".py"
            
            # Finally, translate and write to file:
            translate_and_write(filepath, destination, output_language, **options)
        
    elif "console" in options or filepath is None:
        launch_console(options.pop("console"))
    else:
        # No other option specified: call run_file, which first translates it
        # into regular python and then runs it:
        run_file(
            filepath, 
            encoding=options["encoding"],
            errors=options["errors"]
        )