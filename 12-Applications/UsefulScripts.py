from pathlib import Path as p
from copy import deepcopy
import re

REGX_PATTERN = "( - | )"
REPLACE_WITH = "-"
# Get current directory
rel_path = p.cwd()
# Get all files
files = [file for file in rel_path.iterdir()]
# Get all filenames
names = [file.name for file in files]
# Do type casting for each name
fmt_names = [re.sub(REGX_PATTERN, REPLACE_WITH, name) for name in names]
# Change each file name
for file, name in zip(files, fmt_names):
    file.rename(name)