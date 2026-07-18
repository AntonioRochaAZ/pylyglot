if __name__ == "__main__":
    import sys, os, re, json
    from warnings import warn

    from .config import get_config_path, get_config, set_config, reset_config, options
    from .hooks import install
    from .translator import translate_and_write, run_file, detect_language_from_extension, get_pylyglot_message
    from .console import launch_console

    args = sys.argv

    if len(args) < 2:
        raise SyntaxError(get_pylyglot_message(options["default_language"], "main_arg_length_error"))
    
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
                raise SyntaxError(get_pylyglot_message(options["default_language"], "main_file_specified_twice", filepath=filepath, arg=arg))
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
            raise SyntaxError(get_pylyglot_message(options["default_language"], "main_couldnt_interpret_argument", arg=arg))

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
        raise SyntaxError(get_pylyglot_message(options["default_language"], "main_couldnt_find_filepath"))

    if "console" in options and "translate" in options:
        raise ValueError(get_pylyglot_message(options["default_language"], "main_console_and_translate"))

    # Handle --translate option:
    if "translate" in options:
        destination = options.pop("__destination__", None)
        if destination is None:
            raise SyntaxError(get_pylyglot_message(options["default_language"], "main_translate_destination"))

        output_language = options.pop("translate")
        if str(output_language).lower() == "none":
            # We can identify the language by the extension of the destination:
            lang = detect_language_from_extension(destination)
            if lang is not None :
                if str(options["verbose"]).lower() == "true":
                    warn(get_pylyglot_message(options["default_language"], "main_no_output_language_verbose", lang=lang))
                output_language = lang
            else:
                # if str(options["verbose"]).lower() == "true":
                warn(get_pylyglot_message(options["default_language"], "main_defaulting_to_default_language", default_language=options["default_language"]))
                output_language = options["default_language"]

        if os.path.isdir(filepath):
            if os.path.exists(destination):
                if not os.path.isdir(destination):
                    raise ValueError(get_pylyglot_message(options["default_language"], "main_file_and_destination_type_mismatch", filepath=filepath, destination=destination))
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
            print(get_pylyglot_message(options["default_language"], "main_console_language", default_language=options["default_language"]))
            options["console"] = options["default_language"]
        launch_console(options["console"])
    else:
        # No other option specified: call run_file, which first translates it
        # into regular python and then runs it:
        # TODO: encoding and error options must go into the Loader and console 
        # translation options defined. Must define a global variable for this, then
        run_file(filepath)