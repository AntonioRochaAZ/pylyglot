# Pylyglot: write and run python code on your native language

![](https://antoniorochaaz.github.io/pylyglot/_images/pylyglot.png)

[Pylyglot documentation](https://antoniorochaaz.github.io/pylyglot/)

How come it's 2026 and I can't write code in my own language,
with accents and special characters?

Pylyglot is an extremely simple python package with no dependencies
(other than python itself) which allow you to write "python" code
with keywords from your language. It can be used for teaching,
learning, in serious projects or for fun. Running it is as simple as running: 

``python -m pylyglot your_pylyglot_file``

Pylyglot also handles importing modules from different languages gracefully,
allowing for multilingual projects. 

With the [Pylyglot VSCode extension](https://marketplace.visualstudio.com/items?itemName=AntonioRochaAZ.pylyglot), syntax highlighting is also available for all
supported languages. The language is automatically recognized by the file extension: ``.language_code.py`` (e.g. portuguese_module **.pt.py**).

## Installation

Pylyglot is now available at PyPI !

``pip install pylyglot``

We would like to thank [Aaquinas](https://gitlab.com/Aaquinas) 
for kindly giving up the package name so we could use it in
this project.

## Main features

[Check the feature page!](https://antoniorochaaz.github.io/pylyglot/features.html)

- Language file extensions
- Running pylyglot files directly
- Translate files (and codebases) to and from different languages
- Running a multilingual code base seamlessly
- Interactive console in your language
- Traceback message translation
- Internal pylyglot messages are translated to all available languages
- Smart translation of just the right names
- Security against name clashes and English fallback


## Links

- [Pylyglot documentation](https://antoniorochaaz.github.io/pylyglot/)
- [GitHub repository](https://github.com/AntonioRochaAZ/pylyglot)
- [VSCode extension (marketplace)](https://marketplace.visualstudio.com/items?itemName=AntonioRochaAZ.pylyglot)
- [VSCode extension (source)](https://github.com/AntonioRochaAZ/pylyglot_vscode_extension)
- [PyPI page](https://github.com/AntonioRochaAZ/pylyglot)

## Available languages

| Code | Language | Status | Comment |
|---|---|---|---|
| `ar` | Modern Standard Arabic | Complete (AI generated) | Contributor needed |
| `cs` | Czech | Complete (AI generated) | Contributor needed |
| `da` | Danish | Complete (AI generated) | Contributor needed |
| `de` | German | Complete (AI generated) | Contributor needed |
| `en` | English | Complete | Used for default internal pylyglot messages. |
| `es` | Spanish | Complete (AI generated) | Contributors welcome, verified by a human. |
| `fi` | Standard Finnish (suomi) | Complete (AI generated) | Contributor needed |
| `fr` | French | Complete | Mostly manually translated. Fully verified. |
| `ha` | Hausa | Complete (AI generated) | Contributor needed |
| `hi` | Hindi | Complete (AI generated) | Contributor needed, "uses Devanagari script" |
| `is` | Icelandic | Complete (AI generated) | Contributor needed |
| `it` | Italian | Complete (AI generated) | Contributor needed |
| `ja` | Japanese | Complete (AI generated) | Contributor needed |
| `ko` | Korean | Complete (AI generated) | Contributor needed, "Hangul script" |
| `nb` | Norwegian Bokmål | Complete (AI generated) | Contributor needed |
| `nl` | Dutch | Complete (AI generated) | Contributor needed |
| `pl` | Polish | Complete (AI generated) | Contributor needed |
| `pt` | Portuguese | Complete | Default, points to `pt_br` |
| `pt_br` | Portuguese (Brazil) | Complete | Mostly manually translated. Fully verified. |
| `pt_rj` | Portuguese (Rio de Janeiro) | In progress | Informal (contains slang) |
| `ru` | Russian | Complete (AI generated) | Contributor needed |
| `sv` | Swedish | Complete (AI generated) | Contributor needed |
| `sw` | Swahili | Complete (AI generated) | Contributor needed |
| `uk` | Ukranian | Complete (AI generated) | Contributor needed |
| `yo` | Yoruba | Complete (AI generated) | Contributor needed |
| `zh` | Simplified Chinese | Complete (AI generated) | Contributor needed |