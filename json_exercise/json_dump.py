import json

def save_dict_to_json(filename):
    """
    将字典保存为具有指定文件名的JSON文件。

    :param dict_data: 要保存的字典。
    :param filename: 要保存字典的文件名。.
    ensure_ascii=False 参数确保 Unicode 字符（如中文）被正确写入，而不是被转换为 ASCII 编码
    """
    name = str(input("请输入一个键"))
    value = int(input("请输入一个值"))
    dict_data ={}
    dict_data[name]=value
    with open(filename, "w", encoding="utf8") as file:
        json.dump(dict_data, file, ensure_ascii=False)
    json_dump_type=type(filename)
    return json_dump_type
# 使用例子

if "__main__"==__name__:
    json_type=save_dict_to_json("dict_demo.json")
    print(json_type)

