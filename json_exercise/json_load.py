import json
def load_dict_to_json(filename):
    path=filename
    f=open(path,"r",encoding="utf8")

    result=json.load(f)
    json_load_type=type(result)
    return result,json_load_type

if "__main__"==__name__:

    result,json_type=load_dict_to_json("dict_demo.json")
    print(result,json_type)