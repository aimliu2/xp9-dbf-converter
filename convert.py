import glob
import dbf
import os
from pathlib import Path 
from sqlite_utils import Database

# --------------------------------- Reference -------------------------------- #
# https://pypi.org/project/dbf/

# ------------------------------- 1 Declaration ------------------------------ #
dbf_paths = "DAT_input"
des_path = "DAT_output"

encoders = ["utf8", "cp874"]

# get all dbf in folders
files_path = glob.glob(dbf_paths + "/*.DBF")
# select dbf files
select = ['CUSTOMER','ADMIT','ROOM','RMSERV','ALLCODE', 'SP_RATE', 'DBTH', 'TRANSACT']
thdb = ["CUSTOMER","ALLCODE", "SP_RATE"]

# filter working files
def filterInSelect(x):
    if Path(x).stem in select:
        return True
    else:
        return False

dbf_files_path = list(filter(filterInSelect,files_path))

print('working files: ', dbf_files_path)    

# create Destination Folder first
os.makedirs(des_path, exist_ok=True)

def createDB():
    target_p = os.path.join(des_path, "DAT_output.sqlite")
    db = Database(target_p)
    
    for p in dbf_files_path:
        table_name = Path(p).stem
        print("Processing: {}".format(table_name))
        
        if table_name in thdb:
            table = dbf.Table(str(p), codepage=encoders[1]) # THAI
        else:
            table = dbf.Table(str(p), codepage=encoders[0]) # UTF8
            
        table.open()
        columns = table.field_names
        db[table_name].insert_all(dict(zip(columns, list(row))) for row in table)
        table.close()
        print("Created table: " + table_name)
        
    db.vacuum()
    print("Full database created at: " + target_p)

# ---------------------------------------------------------------------------- #
#                                  Executeion                                  #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    createDB()
