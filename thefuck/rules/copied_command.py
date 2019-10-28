"""Fixes common error when you copy and paste commands from documentation

Example:
> $ git clone https://github.com/nvbn/thefuck.git
bash: $: command not found...
"""

import re

def match(command):
    return ("$: command not found" in command.output and
            re.search(r"^\$[\s]*[\S]+", command.script) is not None)

def get_new_command(command):
    return command.script.replace("$", "", 1).strip()

requires_output = True