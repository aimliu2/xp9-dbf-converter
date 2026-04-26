# Converter Prep Notes

These notes are for preparing and maintaining the Python environment used by `../convert.py`.

## Python Version

Use Python 3.14.

Verified interpreter on this machine:

```bash
~/.pyenv/versions/3.14.0/bin/python
```

Check the version:

```bash
~/.pyenv/versions/3.14.0/bin/python --version
```

## Required Packages

`convert.py` requires:

```text
dbf
sqlite-utils
```

Install them:

```bash
~/.pyenv/versions/3.14.0/bin/python -m pip install dbf sqlite-utils
```

Check that imports work:

```bash
~/.pyenv/versions/3.14.0/bin/python -c "import dbf, sqlite_utils; print('imports ok')"
```

## Optional Requirements File

Create a requirements file from the current environment:

```bash
~/.pyenv/versions/3.14.0/bin/python -m pip freeze > requirements.txt
```

Install from a requirements file:

```bash
~/.pyenv/versions/3.14.0/bin/python -m pip install -r requirements.txt
```

Write an uninstall list:

```bash
~/.pyenv/versions/3.14.0/bin/python -m pip freeze > rm.txt
```

Uninstall packages listed in `rm.txt`:

```bash
~/.pyenv/versions/3.14.0/bin/python -m pip uninstall -r rm.txt -y
```

Use uninstall commands carefully. Prefer a virtual environment if testing new package versions.

## Input Preparation

Place the old FoxPro/DBF files in:

```text
DAT_input/
```

The current converter only imports these tables:

```text
CUSTOMER.DBF
ADMIT.DBF
ROOM.DBF
RMSERV.DBF
ALLCODE.DBF
SP_RATE.DBF
DBTH.DBF
TRANSACT.DBF
```

Other `.DBF` files can exist in `DAT_input/`, but they are ignored unless added to the `select` list in `convert.py`.

## Run The Converter

Run from the parent `dbc` folder:

```bash
cd dbc
PYTHONDONTWRITEBYTECODE=1 ~/.pyenv/versions/3.14.0/bin/python convert.py
```

The output file is:

```text
DAT_output/DAT_output.sqlite
```

## Verify The Output

List tables and counts:

```bash
~/.pyenv/versions/3.14.0/bin/sqlite-utils tables DAT_output/DAT_output.sqlite --counts
```

Inspect schema:

```bash
~/.pyenv/versions/3.14.0/bin/sqlite-utils schema DAT_output/DAT_output.sqlite
```

Inspect sample rows:

```bash
~/.pyenv/versions/3.14.0/bin/sqlite-utils rows DAT_output/DAT_output.sqlite CUSTOMER --limit 5 --nl
```

## Encoding Notes

The converter currently uses:

```text
cp874: CUSTOMER, ALLCODE, SP_RATE
utf8:  other selected tables
```

If Thai text looks broken after conversion, check the DBF codepage first.
