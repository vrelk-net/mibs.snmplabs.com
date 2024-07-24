#!/usr/bin/env python3

# renames all files in the .import directory to the name of the MIB module

import pathlib
import re
import os

print('Processing all files in the .import directory')
print('')

regex = r"^\s*([\w-]+)\s+DEFINITIONS\s+::=\s+BEGIN"
indir = '.import'
outdir = 'asn1'

files = [f for f in pathlib.Path(indir).iterdir() if f.is_file()]

for f in files:
    for i, line in enumerate(open(f)):
        for match in re.finditer(regex, line):
            print('Renaming %s to %s/%s' % (f, outdir, match.group(1)))
            os.replace(f, '%s/%s' % (outdir, match.group(1)))

print('')
print('Renamed %d files' % len(files))
print('Done')
exit(0)
