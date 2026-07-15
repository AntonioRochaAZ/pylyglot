# English: KEEP AS DEFAULT!
dictionary = dict()
traceback_dictionary = dict()

# PYLYGLOT INTERNAL MESSAGES
def pylyglot_version_warning(path, version, current_version):
    return f"Pylyglot file {path} generated with version {version}, but you are using {current_version} for translation! Translation could be inconsistent."

inv_internal_pylyglot_dict = {
    "pylyglot_version_warning": pylyglot_version_warning
}
