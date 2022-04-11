import sqlite3
import functions

def create_data_base(db_fileName):
    conn = sqlite3.connect(db_fileName)
    cursor = conn.cursor()
    return {"conn": conn, "cursor": cursor}

def create_table(table, data_base):
    cursor=data_base["cursor"]
    str_table_name=table['name']
    fields=table['fields']

    sql_prefix="CREATE TABLE IF NOT EXISTS ["""+str_table_name+"] ("

    sql_fields="[ID] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
    for field in fields:
        sql_fields=sql_fields+"["+str(field['name'])+"] "+str(field['type'])+", "
    sql_fields=sql_fields[:-2]

    sql_sufix=")"

    cursor.execute(sql_prefix+sql_fields+sql_sufix)

def drop_table(table, data_base):
    cursor=data_base["cursor"]
    str_table_name=table['name']    
    cursor.execute("DROP TABLE IF EXISTS ["+str_table_name+"]")

def drop_all_tables(data_base):
    cursor=data_base["cursor"]
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables=cursor.fetchall()
    for table in tables:
        if str(table[0])!="sqlite_sequence":
            cursor.execute("DROP TABLE IF EXISTS ["+table[0]+"]")

def insert_datas(table, datas, data_base):
    conn=data_base["conn"]
    cursor=data_base["cursor"]

    str_table_name=table['name']
    fields=table['fields']

    sql_prefix="INSERT INTO ["+str_table_name+"] ("

    sql_fields=""
    sql_interrogation=""
    for field in fields:
        sql_fields=sql_fields+"["+str(field['name'])+"], "
        sql_interrogation=sql_interrogation+"?, "
    sql_fields=sql_fields[:-2]
    sql_interrogation=sql_interrogation[:-2]

    sql_middle=") VALUES ("
    
    sql_sufix=")"

    cursor.executemany(sql_prefix+sql_fields+sql_middle+sql_interrogation+sql_sufix, datas) 
    conn.commit()
    return cursor.lastrowid

def insert_base(datas, name):
    data_base=create_data_base('.\\exports\\states.db')
    drop_all_tables(data_base)

    keys=functions.extract_keys(datas)
    datas=functions.extract_datas(datas, keys)
    
    table={
        "name": name
    }
    fields=[]
    for key in keys:
        field={
            "name": key,
            "type": "TEXT"
        }
        fields.append(field)
    table['fields']=fields

    create_table(table, data_base)
    insert_datas(table, datas, data_base)
