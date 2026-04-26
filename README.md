# DBF To SQLite Converter

This folder contains the old BillXP9 data converter. It reads selected FoxPro/DBF tables from `DAT_input/` and creates one SQLite database at:

```text
DAT_output/DAT_output.sqlite
```

The converter is still valid as the starting point for the BillXP10 DBF import sidecar.

## Requirements

Use Python 3.14.

Required Python packages:

```text
dbf
sqlite-utils
```

If the packages are missing:

```bash
python -m pip install dbf sqlite-utils
```

On this machine, the verified interpreter is:

```bash
~/.pyenv/versions/3.14.0/bin/python
```

## Folder Layout

```text
dbc/
  convert.py
  DAT_input/
    CUSTOMER.DBF
    ADMIT.DBF
    ROOM.DBF
    RMSERV.DBF
    ALLCODE.DBF
    SP_RATE.DBF
    DBTH.DBF
    TRANSACT.DBF
  DAT_output/
    DAT_output.sqlite
```

Only these DBF tables are converted by the current script:

```text
CUSTOMER
ADMIT
ROOM
RMSERV
ALLCODE
SP_RATE
DBTH
TRANSACT
```

## Run

Run the script from this folder. The script uses relative paths, so running it from another directory will not find `DAT_input/`.

```bash
cd dbc
PYTHONDONTWRITEBYTECODE=1 ~/.pyenv/versions/3.14.0/bin/python convert.py
```

Expected result:

```text
Full database created at: DAT_output/DAT_output.sqlite
```

## Verified Output

Last verified with Python 3.14.0.

Expected table counts from the current `DAT_input/` set:

```text
SP_RATE    372
ADMIT      88
DBTH       15977
ALLCODE    338
TRANSACT   3125
ROOM       64
RMSERV     66
CUSTOMER   1099
```

Thai text was spot-checked in `CUSTOMER`, `ALLCODE`, and `SP_RATE`.

## Notes

- `CUSTOMER`, `ALLCODE`, and `SP_RATE` are opened with `cp874` for Thai text.
- Other selected tables are opened as `utf8`.
- The output is one SQLite database containing all selected tables.
- Re-running the converter recreates/writes the output database path.

See [prep/readme.md](prep/readme.md) for setup and cleanup notes.
