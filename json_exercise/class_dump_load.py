import json
class Zjx:
    def __init__(self,filename):
        self.filename=filename
    def save_dict_to_json(self):
        """
        将字典保存为具有指定文件名的JSON文件。

        :param dict_data: 要保存的字典。
        :param filename: 要保存字典的文件名。.
        """
        name = str(input("请输入一个键"))
        value = int(input("请输入一个值"))
        dict_data = {}
        dict_data[name] = value
        with open(self.filename, "w", encoding="utf8") as file:
            json.dump(dict_data, file, ensure_ascii=False)
            # ensure_ascii=False 参数确保 Unicode 字符（如中文）被正确写入，而不是被转换为 ASCII 编码
        json_dump_type = type(self.filename)
        return json_dump_type

    def load_dict_to_json(self):
        path = self.filename
        f = open(path, "r", encoding="utf8")

        result = json.load(f)
        json_load_type = type(result)
        return result, json_load_type

if "__main__"==__name__:
    p1=Zjx("dict_json_demo.json")
    json_dump_out1=p1.save_dict_to_json()
    result,json_load_out=p1.load_dict_to_json()
    print(result)