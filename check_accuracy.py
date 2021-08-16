import os
import re
from posixpath import split
file_path = "xml_annotations"

xml_list = os.listdir(file_path)

for p in xml_list:
    xml_name = file_path + '/' + p
    with open(xml_name, "r") as f:
        data = f.read()

        data_list = []
        for a in re.finditer("<name>", data) :
            data_list.append(data_list[a.start():a.end()])
        print(len(data_list))
