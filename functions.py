from unidecode import unidecode

def clear_string(origin):
    origin=origin.rstrip()
    return origin

def tratament_string(origin):
    origin=clear_string(origin)
    origin=unidecode(origin)
    origin=origin.lower()
    origin=origin.replace("[", "").replace("]", "")
    origin=origin.replace(" ", "_")
    return origin
    
def extract_keys(datas):
    keys=[]
    for data in datas:
        keys=keys+list(data.keys())
    return list(dict.fromkeys(keys))

def extract_datas(datas, fields):
    clear_datas=[]
    for data in datas:
        array_data=[]
        for field in fields:
            if field in data.keys():
                array_data.append(data[field ])
            else:
                array_data.append(None)
        clear_datas.append(array_data)
    return clear_datas

