import json
dict_json={"王二":21,"麻子":22}

dict_str=json.dumps(dict_json)
print(type(dict_str))

dict_loads=json.loads(dict_str)
print(type(dict_loads))