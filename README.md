# mibs.snmplabs.com

Scrape of all MIBs taken from http://mibs.snmplabs.com/asn1/, as of 01/31/2020.

Created with a recursive wget command.

This repo only exists because those sources don't seem to be in github.

All original MIB files are in the 'asn1' directory.

All compiled MIB .py files are in the 'pysnmp' directory.

If you wish to add new MIBs, place them in the '.import' directory, then run `make import`.

# Instructions

```
# Create the Python enviroment
pipenv shell
pipenv install

# Import new MIBs
make import

# Comiling all mibs
make compile
make compile-json
make compile-with-texts

# Compiling mibs only updated and just added
make compile-changed
make compile-json-changed
make compile-with-texts-changed
```
