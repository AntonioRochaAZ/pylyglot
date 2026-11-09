import re
import json

# COMMENT_RE = re.compile(r"^([^(//)]*)//") # To complexify later (avoid this if "//" is in a string)
COMMENT_RE = re.compile(r'^((?:"(?:\\.|[^"\\])*"|[^"])*)//.*$')

def load(f, debug: bool = False):
    lines = f.readlines()
    for i, line in enumerate(lines):
        match = COMMENT_RE.match(line)
        if match is not None:
            lines[i] = match.group(1)
    plain_text = "\n".join(lines)
    if debug: print(plain_text)
    try:
        dictionary = json.loads(plain_text)
    except Exception as e:
        print(plain_text)
        raise e
    return dictionary