if __name__ == "__main__":
    import sys, os, re
    from importlib.metadata import version, PackageNotFoundError 
    from .translator import get_dictionary, translate_file, run_file 
    from .hooks import install
    install()

    args = sys.argv

    if len(args) < 2:
        raise SyntaxError("pylyglot must receive at least 1 options: the path to the file.")
    
    # Ignore current file name:
    args = args[1:]
    
    input_language = None
    filepath = None
    options  = {"encoding": "utf-8", "errors": "strict", "output-encoding": "utf-8"}  # default values
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
                raise SyntaxError(f"File path specified twice? {filepath}, {arg}.")
            if filepath is None:
                # First time we find an existing file path, must be the source file
                filepath = os.path.abspath(arg)
            else:
                options["__destination__"] = os.path.abspath(arg)
        else:
            raise SyntaxError(f"Couldn't interpret argument: {arg}. Make sure you have provided the right paths.")
    
    if filepath is None and "console" not in options:
        raise SyntaxError("Could not identify filepath in command line arguments.")

    if "input-language" in options:
        # Check if it is a valid language to translate to:
        if str(options["input-language"]).lower() == "none": options["input-language"] = None
        if options["input-language"] is not None:
            d = get_dictionary(options["input-language"], throw_exception=False)
            if d is not None:
                # It is a valid language str
                input_language = options["input-language"]
            else:
                raise ValueError(
                    f"Input language specified with --input-language, but value ({value}) does not correspond to an implemented language.\n"
                    # f"Implemented languages: {os.listdir()}"
                )
        else:
            input_language = None
    # language is potentially none and will be infered either by 1. comment at 
    # the beginning of the file or 2. the file extension (in that order of preference).
    # if input_language is None:
    #     input_language = detect_language(filepath, encoding=options["encoding"], errors=options["errors"])

    # Handle --translate option
    if "translate" in options:
        output_language = options.pop("translate")
        if str(output_language).lower() == "none": output_language = None
        destination = options.pop("__destination__", None)
        if destination is None:
            raise SyntaxError("--translate requires a destination: python -m pylyglot --translate=language src dst")

        def translate_and_write(src_path: str, dst_path: str):
            """
            Translate file from one language to another, adding a line comment specifying its language 
            at the beginning of it.
            """

            translated = translate_file(
                src_path, 
                output_language=output_language, 
                input_language=input_language,
                encoding=options["encoding"],
                errors=options["errors"]
            )

            try:
                current_version = version("pylyglot")
            except PackageNotFoundError:
                current_version = "unknown"
            
            header = f"# pylyglot: {output_language} # version: {current_version} #\n"
            lines = translated.splitlines(keepends=True)
            # Check for the #!/bin/sh-type line and keep it if it is the case.
            if lines and lines[0].startswith("#!"):
                output = lines[0] + header + "".join(lines[1:])
            else:
                output = header + translated

            # Make directory path if not existant:
            os.makedirs(os.path.dirname(dst_path) or ".", exist_ok=True)
            # Write file:
            with open(dst_path, "w", encoding=options["output-encoding"]) as f:
                f.write(output)
            print(f"Translated: {src_path} into {dst_path}.")

        if os.path.isdir(filepath):
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
                    translate_and_write(src_path, dst_path)
        else:
            # Input is NOT a folder
            # if destination doesn't already have the language extension, add it
            if output_language is not None:
                if not destination.endswith(f'.{output_language}.py'):
                    base = re.sub(r"(\.[a-z_]*)?\.py$", '', destination) # Eventually correcting the extension
                    destination = f'{base}.{output_language}.py'
            else:
                if not destination.endswith(f'.py'):
                    destination = destination+".py"

            translate_and_write(filepath, destination)
    elif "console" in options or filepath is None:
        from .console import launch_console
        launch_console(input_language or options.get("console"))
    else:
        # No other option specified: call run_file, which first translates it
        # into regular python and then runs it:
        run_file(
            filepath, 
            input_language,
            encoding=options["encoding"],
            errors=options["errors"]
        )