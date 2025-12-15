# Python setup

## Python install requirement.txt
`pip install -r requirements.txt`

## Python export requirement.txt
`pip freeze > rm.txt` will get all libraries w/o **wheel and setuptool**

## Python uninstall all libs in files
`pip uninstall -r rm.txt -y.`


# How it works
1. move all `.DBF` from `Data/*` folder to `1_convertDB` using `1move.sh`
- move `.db` from `2clean/Dat_sql/*` to `3napp/Billxp9` using `2move.sh`