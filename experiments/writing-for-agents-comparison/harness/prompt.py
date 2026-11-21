"""Print a wrapper prompt verbatim with <DIR> filled in.

  prompt.py <prompt-file> <block-number> <dir>

Prompt files hold one or more prompts, each starting after a line '---'
and running to the next '## ' heading or the end of the file.
"""
import re
import sys

path, block, directory = sys.argv[1], int(sys.argv[2]), sys.argv[3]
text = open(path).read()
blocks = []
for part in text.split("\n---\n")[1:]:
    blocks.append(re.split(r"\n## ", part)[0].strip())
print(blocks[block].replace("<DIR>", directory))
