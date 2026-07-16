if __name__ == "__main__":
    import sys, os, re, json
    from warnings import warn

    from .config import get_config_path, get_config, set_config, reset_config, options
    from .hooks import install
    from .translator import translate_and_write, run_file, detect_language_from_extension
    from .console import launch_console

    args = sys.argv

    if len(args) < 2:
        raise SyntaxError("pylyglot must receive at least 1 options: the path to the file.") # TODO: convert this to a language dependent thing.
    
    # Ignore current file name:
    args = args[1:]
    
    # Getting options:
    filepath = None
    """
    We also have a few mutually exclusive options:
    --translate=<output_language>
    --console=<console_input_language>
    --setconfig <config_key>=<config_value>
    --getconfig
    --getconfigpath
    --resetconfig
    """
    lookup_idx = 1
    for arg_idx, arg in enumerate(args):
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
        elif args[arg_idx - lookup_idx] == "--setconfig":
            option, value = arg.split("=")
            set_config(option, value)
            lookup_idx += 1
        else:
            raise SyntaxError(f"Couldn't interpret argument: {arg}. Make sure you have provided the right paths.") # TODO: convert this to a language dependent thing.


    # Now that options have been updated, we can install
    # the custom hooks to allow imports from other languages:
    install()

    # setconfig option must come first as it has alerady been run:
    # TODO: add message saying that we are ignoring other options.
    if "setconfig" in options:
        sys.exit(0) # Exit program immediately
    
    if "getconfig" in options:
        print(json.dumps(get_config(), indent=4))
        sys.exit(0) # Exit program immediately.

    if "getconfigpath" in options:
        print(get_config_path())
        sys.exit(0) # Exit program immediately
    
    if "resetconfig" in options:
        reset_config()
        sys.exit(0)

    # Handling unexpected options:
    if filepath is None and "translate" in options:
        raise SyntaxError("Could not identify filepath in command line arguments.") # TODO: convert this to a language dependent thing.

    if "console" in options and "translate" in options:
        raise ValueError('pylyglot received both "console" and "translate" options at the same time (only one allowed).') # TODO: convert this to a language dependent thing.

    # Handle --translate option:
    if "translate" in options:
        destination = options.pop("__destination__", None)
        if destination is None:
            raise SyntaxError("--translate requires a destination: python -m pylyglot --translate=output_language source_path destination_path") # TODO: convert this to a language dependent thing.

        output_language = options.pop("translate")
        if output_language is None: # Happens if the user just passes "--translate"
            # We can identify the language by the extension of the destination:
            lang = detect_language_from_extension(destination)
            if lang is not False:
                # if str(options["verbose"]).lower() == "true":
                warn(f'No output language was specified for the translate option. Language identified by the file extension: {lang}.') # TODO: convert this to a language dependent thing.
                output_language = lang
            else:
                # if str(options["verbose"]).lower() == "true":
                warn(f'No output language was specified for the translate option, translating to default language: {options["default_language"]}.') # TODO: convert this to a language dependent thing.
                output_language = options["default_language"]
        
        if str(output_language).lower() == "none": 
            print(
                f'PylyglotWarning: No output language specified, using default langauge: {options["default_language"]}.'
                '\nYou can change the default language by running "python -m pylyglot --setconfig default_langauge=language_code".'
            ) # TODO: translate (potentially have a language name instead of just the code).
            output_language = options["default_language"]
        
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
        
    elif "console" in options:
        if str(options["console"]).lower() == "none":
            print(
                f'PylyglotWarning: No output language specified, using default langauge: {options["default_language"]}.'
                '\nYou can change the default language by running "python -m pylyglot --setconfig default_langauge=language_code".'
            ) # TODO: translate (potentially have a language name instead of just the code).
            options["console"] = options["default_language"]
        launch_console(options["console"])
    else:
        # No other option specified: call run_file, which first translates it
        # into regular python and then runs it:
        # TODO: encoding and error options must go into the Loader and console 
        # translation options defined. Must define a global variable for this, then
        run_file(filepath)