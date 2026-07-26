# Pylyglot: write and run python code on your native language

![](docs/en/source/_static/overview.png)

[> Documentation <](https://antoniorochaaz.github.io/pylyglot/)

Pylyglot is an extremely simple python package with no dependencies
(other than python itself) which allow you to write "python" code
with keywords from your language. Running it is as simple as running: 

``python -m pylyglot your_module.py``

Pylyglot also handles importing multilingual modules gracefully. 

With the [Pylyglot VSCode extension](https://marketplace.visualstudio.com/items?itemName=AntonioRochaAZ.pylyglot), syntax highlighting is also available for all
supported languages. The language is automatically recognized by the file extension: ``.language_code.py`` (e.g. portuguese_module **.pt.py**).

## Links

- [Pylyglot GitHub](https://github.com/AntonioRochaAZ/pylyglot)
- [Pylyglot documentation](https://antoniorochaaz.github.io/pylyglot/)
- [VSCode extension (marketplace)](https://marketplace.visualstudio.com/items?itemName=AntonioRochaAZ.pylyglot)
- [VSCode extension (source)](https://github.com/AntonioRochaAZ/pylyglot_vscode_extension)

## Main features

## Installation

### pip

Pylyglot is not (yet) at PyPI, but will be soon. However, it is already available from Test PyPI 
(the sandboxed version of PyPI which is used for testing) and can be installed with:

``pip install -i https://test.pypi.org/simple/ pylyglot``

### From source
```
git clone https://github.com/AntonioRochaAZ/pylyglot.git
cd pylyglot
pip install .
```

# Documentation

[Check all features and the full documentation here!](https://antoniorochaaz.github.io/pylyglot/)

