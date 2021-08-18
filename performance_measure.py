import os
import re
from xml.etree.ElementTree import parse

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np


file_path = "xml_annotations"

xml_list = os.listdir(file_path)

# for p in xml_list:
#   xml_name = file_path + '/' + p

xml_name = file_path + '/' +"lg-46690-aug-gutenberg1939-.xml"

tag_tree = parse(xml_name)
tag_root = tag_tree.getroot()

datas = tag_root[4:]

# X=np.array([0,1])
# Y=np.array([0,1])
# plt.plot(X,Y,color='None')

# for obj in datas:
#     xmin = float(obj[1][0].text)
#     xmax = float(obj[1][1].text)
#     ymin = float(obj[1][2].text)
#     ymax = float(obj[1][3].text)
    

#     shp=patches.Rectangle((xmin, ymin), xmax-xmin,ymax-ymin, color='b')
#     plt.gca().add_patch(shp)

# plt.show()

for obj in datas:
    xmin = float(obj[1][0].text)
    xmax = float(obj[1][1].text)
    ymin = float(obj[1][2].text)
    ymax = float(obj[1][3].text)

    

