import cv2
import glob
import os
import subprocess
import shutil
import numpy as np
import math
from enum import Enum, auto
import copy
from itertools import chain
import time
import subprocess
from IPython.display import Image, clear_output  # to display images
##
from bfaaap.leveloriginalimg.leveloriginalimg import leveloriginalimg
from bfaaap.alignmeasures.align_measures import generate_measures_in_eachstave_aslist
from bfaaap.enlargemeasures.enlargeeachmeasure import produceResizedMeasuresFromAlignedStaves
from bfaaap.leveloriginalimg.leveloriginalimg import leveleachmeasure
import matplotlib.pyplot as plt
from PIL import Image
from bfaaap.makeyolomusicdict.generatedictforxml import setCurrentAccidentalTable, generateMSsequenceForStaff1or2, Clef
from bfaaap.makeyolomusicdict.generatedictforxml import generateDictForET_singlestaff
from bfaaap.makeyolomusicdict.generatedictforxml import give_all_ms_in_eachmeasure_for_staff1or2

from bfaaap.yoloToxml.yoloToxml import musicData2XML
import xml.etree.ElementTree as ET
from xml.dom import minidom

def show_images(images, figsize=(20,20), columns = 4):
    plt.figure(figsize=figsize)
    for i, image in enumerate(images):
        plt.subplot(len(images) / columns + 1, columns, i + 1)
        plt.imshow(image)

#here, provide a FILE_PATH for a sheet music image (either .jpg or .png)
FILE_PATH ='./bfaaap/musicdata/test0/test.jpg'
#input base data for sheet music of interest:
tempo = 120 #
fifths = -1 #if the key signature after clef has three #, the number is 3 (positive integer); if the key signature has one b, the number is -1 (negative integer); if the key signature does't have any of them, the number is 0
beats = 3 #if the beat is 3/4, the "beats" is 3 and the "beat_type" is 4. 
beat_type = 2 #see the above
preset_measure_duration = 1024 * beats / beat_type #

########
#Image(filename=FILE_PATH, width=250) 
showimg = Image.open(FILE_PATH)
#showimg.show()

FILE_PATH = leveloriginalimg(FILE_PATH)

#Image(filename=FILE_PATH, width=250) 
showimg = Image.open(FILE_PATH)
#showimg.show()

#######

#extract staves with measures
#perform inference on sheet music
SAVE_DIRECTORY_PATH = os.path.dirname(FILE_PATH) + '/staff'

proc = subprocess.Popen(['python','./bfaaap/yolov5/detect.py', '--weights', './bfaaap/yolov5/weightsstock/last_0.95_staff4_20201230.pt', '--SAVE_PATH', SAVE_DIRECTORY_PATH ,'--img', '416', '--conf', '0.75', '--source', FILE_PATH, '--save-txt'])
proc.wait()
########
# check the measure inference result
files_temp = glob.glob(FILE_PATH)
#the resulting file after inference of measures
MEASURE_INFERENCE_RESULT_PATH = ''
for file_temp in files_temp:
    if file_temp.endswith('jpg') or file_temp.endswith('png'):
        basename = os.path.basename(file_temp)
        MEASURE_INFERENCE_RESULT_PATH = SAVE_DIRECTORY_PATH + '/' + basename
#show the measure inference results on the leveled sheet music image
#Image(filename=MEASURE_INFERENCE_RESULT_PATH, width=900) 
showimg = Image.open(MEASURE_INFERENCE_RESULT_PATH)
showimg.show()

#After the measure-recognizing model is applied to a piece of sheet music

#copy and move the relevant files under a dirctory ./musicdata/AAA/(staff/labels)
#sheet music (.jpg) provided in FILE_PATH
files_temp = glob.glob(FILE_PATH)
#To skip .txt files
for file_temp in files_temp:
    if file_temp.endswith('jpg') or file_temp.endswith('png'):
        img = cv2.imread(file_temp)
        dirname = os.path.dirname(file_temp)
        basename = os.path.basename(file_temp)
        cv2.imwrite(dirname + '/staff/labels/' + basename, img)
###

#sheet music provided in FILE_PATH
staves_with_measures_in_sheetmusic = generate_measures_in_eachstave_aslist(FILE_PATH)
print(f'the number of staves_with_measures_in_sheetmusic is {len(staves_with_measures_in_sheetmusic)}')
for i, each_staff in enumerate(staves_with_measures_in_sheetmusic):
    print(f'the number of measures in staff{i} is {len(each_staff)}')
###
#input whether staves are paired
areStavesPaired = True

#excise and enlarge each measure img at 412 x 412 pixels in each staff and stored in musicdata/AAA/measure/staff1/ or staff2/

#in the case of wide staff extraction, set staff_magnification = 1.2
staff_magnification = 1.2

produceResizedMeasuresFromAlignedStaves(img_FILE_PATH=FILE_PATH, aligned_staves=staves_with_measures_in_sheetmusic, isPaired=areStavesPaired, upper_margin=staff_magnification, lower_margin=staff_magnification)
###

#level again each measure one by one

MEASURES_STAFF1_PATH = os.path.dirname(FILE_PATH) + '/measure/staff1/*'
files_temp = glob.glob(MEASURES_STAFF1_PATH)
for file_temp in files_temp:
    if file_temp.endswith('jpg') or file_temp.endswith('png'):
        FILE_DIR_PATH = os.path.dirname(file_temp)
        FILE_BASENAME = os.path.basename(file_temp)
        THIS_PATH = FILE_DIR_PATH + '/' + FILE_BASENAME
        result0 = leveleachmeasure(THIS_PATH)

MEASURES_STAFF2_PATH = os.path.dirname(FILE_PATH) + '/measure/staff2/*'
files_temp = glob.glob(MEASURES_STAFF2_PATH)
for file_temp in files_temp:
    if file_temp.endswith('jpg') or file_temp.endswith('png'):
        FILE_DIR_PATH = os.path.dirname(file_temp)
        FILE_BASENAME = os.path.basename(file_temp)
        THIS_PATH = FILE_DIR_PATH + '/' + FILE_BASENAME
        leveleachmeasure(THIS_PATH)

###############
#apply individual models to the measures selected for staff 1 or 2

#work at the yolov5 directory
#%cd /content/img2xml/bfaaap/yolov5

#processes in series (or in parallel)
start = time.time()
print(start)
#processes = []

#image source directory path for either staff1 or staff2


#For staff1


SOURCE_PATH = os.path.dirname(FILE_PATH) + '/measure/staff1/*'

#body
print('processing body 1')
SAVE_DIRECTORY_PATH = os.path.dirname(FILE_PATH) + '/staff1/body'
proc = subprocess.Popen(['python','./bfaaap/yolov5/detect.py', '--weights', './bfaaap/yolov5/weightsstock/last_0.94_body4_20210208.pt', '--SAVE_PATH', SAVE_DIRECTORY_PATH ,'--img', '416', '--conf', '0.60', '--source', SOURCE_PATH, '--save-txt', '--device', '0'])
proc.wait()
#processes.append((0, proc))

#armbeam
print('processing armbeam 1')
SAVE_DIRECTORY_PATH = os.path.dirname(FILE_PATH) + '/staff1/armbeam'
proc = subprocess.Popen(['python','./bfaaap/yolov5/detect.py', '--weights', './bfaaap/yolov5/weightsstock/last_0.99_armbeam2_20210214.pt', '--SAVE_PATH', SAVE_DIRECTORY_PATH ,'--img', '416', '--conf', '0.60', '--source', SOURCE_PATH, '--save-txt', '--device', '0'])
proc.wait()
#processes.append((1, proc))

#accidental
print('processing accidental 1')
SAVE_DIRECTORY_PATH = os.path.dirname(FILE_PATH) + '/staff1/accidental'
proc = subprocess.Popen(['python','./bfaaap/yolov5/detect.py', '--weights', './bfaaap/yolov5/weightsstock/last_0.99_Accidental2_20210209.pt', '--SAVE_PATH', SAVE_DIRECTORY_PATH ,'--img', '416', '--conf', '0.60', '--source', SOURCE_PATH, '--save-txt'])
proc.wait()
#processes.append((2, proc))

#rest
print('processing rest 1')
SAVE_DIRECTORY_PATH = os.path.dirname(FILE_PATH) + '/staff1/rest'
proc = subprocess.Popen(['python','./bfaaap/yolov5/detect.py', '--weights', './bfaaap/yolov5/weightsstock/last_0.99_rest1_20210107.pt', '--SAVE_PATH', SAVE_DIRECTORY_PATH ,'--img', '416', '--conf', '0.60', '--source', SOURCE_PATH, '--save-txt'])
proc.wait()
#processes.append((3, proc))

#clef
print('processing clef 1')
SAVE_DIRECTORY_PATH = os.path.dirname(FILE_PATH) + '/staff1/clef'
proc = subprocess.Popen(['python','./bfaaap/yolov5/detect.py', '--weights', './bfaaap/yolov5/weightsstock/last_0.99_Clef3_20210129.pt', '--SAVE_PATH', SAVE_DIRECTORY_PATH ,'--img', '416', '--conf', '0.60', '--source', SOURCE_PATH, '--save-txt'])
proc.wait()
#processes.append((4, proc))

#For staff2

SOURCE_PATH = os.path.dirname(FILE_PATH) + '/measure/staff2/*'

#body
print('processing body 2')
SAVE_DIRECTORY_PATH = os.path.dirname(FILE_PATH) + '/staff2/body'
proc = subprocess.Popen(['python','./bfaaap/yolov5/detect.py', '--weights', './bfaaap/yolov5/weightsstock/last_0.94_body4_20210208.pt', '--SAVE_PATH', SAVE_DIRECTORY_PATH ,'--img', '416', '--conf', '0.60', '--source', SOURCE_PATH, '--save-txt'])
proc.wait()
#processes.append((5, proc))

#armbeam
print('processing armbeam 2')
SAVE_DIRECTORY_PATH = os.path.dirname(FILE_PATH) + '/staff2/armbeam'
proc = subprocess.Popen(['python','./bfaaap/yolov5/detect.py', '--weights', './bfaaap/yolov5/weightsstock/last_0.99_armbeam2_20210214.pt', '--SAVE_PATH', SAVE_DIRECTORY_PATH ,'--img', '416', '--conf', '0.60', '--source', SOURCE_PATH, '--save-txt'])
proc.wait()
#processes.append((6, proc))

#accidental
print('processing accidental 2')
SAVE_DIRECTORY_PATH = os.path.dirname(FILE_PATH) + '/staff2/accidental'
proc = subprocess.Popen(['python','./bfaaap/yolov5/detect.py', '--weights', './bfaaap/yolov5/weightsstock/last_0.99_Accidental2_20210209.pt', '--SAVE_PATH', SAVE_DIRECTORY_PATH ,'--img', '416', '--conf', '0.60', '--source', SOURCE_PATH, '--save-txt'])
proc.wait()
# processes.append((7, proc))

#rest
print('processing rest 2')
SAVE_DIRECTORY_PATH = os.path.dirname(FILE_PATH) + '/staff2/rest'
proc = subprocess.Popen(['python','./bfaaap/yolov5/detect.py', '--weights', './bfaaap/yolov5/weightsstock/last_0.99_rest1_20210107.pt', '--SAVE_PATH', SAVE_DIRECTORY_PATH ,'--img', '416', '--conf', '0.60', '--source', SOURCE_PATH, '--save-txt'])
proc.wait()
#processes.append((8, proc))

#clef
print('processing clef 2')
SAVE_DIRECTORY_PATH = os.path.dirname(FILE_PATH) + '/staff2/clef'
proc = subprocess.Popen(['python','./bfaaap/yolov5/detect.py', '--weights', './bfaaap/yolov5/weightsstock/last_0.99_Clef3_20210129.pt', '--SAVE_PATH', SAVE_DIRECTORY_PATH ,'--img', '416', '--conf', '0.60', '--source', SOURCE_PATH, '--save-txt'])
proc.wait()
# processes.append((9, proc))

#for i, p in processes:
#    print(f'waiting process {i} to finish')
#    p.wait()

#end the time measurement
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

DISPLAY_FIG_PATHDIR = os.path.dirname(FILE_PATH)
images = []
featureTypes = ['body', 'armbeam', 'clef', 'accidental', 'rest']
numberOfFigs_eachType = 4

#staff1
for feature in featureTypes:
    for i in range(numberOfFigs_eachType):
        #img = Image.open(f'{DISPLAY_FIG_PATHDIR}/staff1/{feature}/measure#{i:03}.jpg')
        img = Image.open(f'{DISPLAY_FIG_PATHDIR}/staff1/{feature}/measure#{i:03}.'+FILE_PATH[-3:])
        images.append(img)
# #change /test0/ to your folder of interest
# img = Image.open('/content/img2xml/bfaaap/musicdata/test0/staff1/body/measure#000.jpg')
# images.append(img)

show_images(images)

images = []

#staff2
for feature in featureTypes:
    for i in range(numberOfFigs_eachType):
        img = Image.open(f'{DISPLAY_FIG_PATHDIR}/staff2/{feature}/measure#{i:03}.'+FILE_PATH[-3:])
        images.append(img)
# #change /test0/ to your folder of interest
# img = Image.open('/content/img2xml/bfaaap/musicdata/test0/staff2/body/measure#000.jpg')
# images.append(img)

show_images(images)
###
#get the file path, basename, extention

files_temp = glob.glob(FILE_PATH) #"./tmp/*":beforehand prepare images and Yolov5 anotation files in ./tmp/subdirectory
#To skip .txt files
FILE_DIR_PATH = ''
FILE_BASENAME = ''
FILE_BASENAME_WITHOUTEXT = ''
for file_temp in files_temp:
    if file_temp.endswith('jpg') or file_temp.endswith('png'):
        img = cv2.imread(file_temp)
        FILE_DIR_PATH = os.path.dirname(file_temp)
        FILE_BASENAME = os.path.basename(file_temp)
        FILE_BASENAME_WITHOUTEXT = os.path.splitext(FILE_BASENAME)[0]
        cv2.imwrite(FILE_DIR_PATH + '/staff/labels/' + FILE_BASENAME, img)
        
#sheet music provided in FILE_PATH
staves_with_measures_in_sheetmusic = generate_measures_in_eachstave_aslist(FILE_PATH)
print(f'the number of staves_with_measures_in_sheetmusic is {len(staves_with_measures_in_sheetmusic)}')
for i, each_staff in enumerate(staves_with_measures_in_sheetmusic):
    print(f'the number of measures in staff{i} is {len(each_staff)}')

#input wheter staves are paired
areStavesPaired = True

#generate ms sequence in each staff


all_ms_in_eachmeasure_staff1, all_ms_in_eachmeasure_staff2 = give_all_ms_in_eachmeasure_for_staff1or2(isPaired=areStavesPaired, aligned_staves_input=staves_with_measures_in_sheetmusic, img_FILE_PATH=FILE_PATH)
print(f'the number of items in all_ms_in_eachmeasure_staff1 is {len(all_ms_in_eachmeasure_staff1)}')
aaa1 = all_ms_in_eachmeasure_staff1['measure#001']
print(f'aaa1 is {aaa1}')
print(f'the number of items in all_ms_in_eachmeasure_staff2 is {len(all_ms_in_eachmeasure_staff2)}')
bbb1 = all_ms_in_eachmeasure_staff2['measure#001']
print(f'bbb1 is {bbb1}')

#This information has been moved to the location where FILE_PATH was input
# #input base data for sheet music of interest:
# tempo = 120 #public data
# fifths = -1 #public data
# beats = 3 #public data
# beat_type = 2 #public data
# preset_measure_duration = 1024 * beats / beat_type #public data

#additional parameters
staff = 1
isWideStaff = False

#classはimportすること
current_clef = Clef.G
current_accidental_table_template ={'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':''}
current_accidental_table = setCurrentAccidentalTable(current_accidental_table_template, fifths)
ms_sequenceOfInterest_staff1 = generateMSsequenceForStaff1or2(all_ms_in_eachmeasure_input=all_ms_in_eachmeasure_staff1, current_accidental_table_input=current_accidental_table, staff=1, current_clef_input=current_clef, preset_measure_duration=preset_measure_duration, FILE_PATH=FILE_PATH, isWideStaff=isWideStaff)

#for staff2: check current_clef
current_clef = Clef.F
ms_sequenceOfInterest_staff2 = generateMSsequenceForStaff1or2(all_ms_in_eachmeasure_input=all_ms_in_eachmeasure_staff2, current_accidental_table_input=current_accidental_table, staff=2, current_clef_input=current_clef, preset_measure_duration=preset_measure_duration, FILE_PATH=FILE_PATH, isWideStaff=isWideStaff)

print(f'the number of items in all_ms_in_eachmeasure_staff1 is {len(all_ms_in_eachmeasure_staff1)}')
print(f'the number of items in all_ms_in_eachmeasure_staff2 is {len(all_ms_in_eachmeasure_staff2)}')

print(f'the number of items in ms_sequenceOfInterest_staff1 is {len(ms_sequenceOfInterest_staff1)}')
print(f'the number of items in ms_sequenceOfInterest_staff2 is {len(ms_sequenceOfInterest_staff2)}')

# generate a dictionary for ET

#for staff1
current_staff1_clef = Clef.G
dictionary_for_ET_staff1 = generateDictForET_singlestaff(ms_sequenceOfInterest_staff_input=ms_sequenceOfInterest_staff1, tempo=tempo, beats=beats, beat_type=beat_type, fifths=fifths, clef=current_staff1_clef)
part_content1 = dictionary_for_ET_staff1['part']
print(f'the number of items in dictionary_for_ET_staff1[0] is \n{len(part_content1)}')
#for staff2
current_staff2_clef = Clef.F
dictionary_for_ET_staff2 = generateDictForET_singlestaff(ms_sequenceOfInterest_staff_input=ms_sequenceOfInterest_staff2, tempo=tempo, beats=beats, beat_type=beat_type, fifths=fifths, clef=current_staff2_clef)
part_content2 = dictionary_for_ET_staff2['part']
print(f'the number of items in dictionary_for_ET_staff2[0] is \n{len(part_content2)}')

print(f'current_staff1_clef:{current_staff1_clef}\ncurrent_staff2_clef:{current_staff2_clef}')


#generate XML



#for staff1

part_et = ET.Element('part')
part_et.attrib = {'id':'P1'}
part_et_1 = musicData2XML(part_et, dictionary_for_ET_staff1)

xmlstr_1 = minidom.parseString(ET.tostring(part_et_1)).toprettyxml(indent="   ")

#to delete <?xml version="1.0"　?> in line 1
xmlstr_1 = xmlstr_1[23:]
            

#read template.xml to prepare part_et XML data and generate the whole XML
wholeXML_staff1_text = ""
with open("./bfaaap/yoloToxml/template.xml", 'r') as f:
    template_text = f.read()
    wholeXML_staff1_text = template_text +'\n' + xmlstr_1 +'\n</score-partwise>'

#save the resulting xml in ./xml/ directory
FILE_DIR_PATH
new_dir_path = FILE_DIR_PATH + '/xml'
os.makedirs(new_dir_path, exist_ok=True)
new_xml_filepath = new_dir_path + '/' + FILE_BASENAME_WITHOUTEXT + '_staff1.xml'
with open(new_xml_filepath, 'w') as f:
    f.write(wholeXML_staff1_text)


#for staff2

part_et = ET.Element('part')
part_et.attrib = {'id':'P1'}
part_et_2 = musicData2XML(part_et, dictionary_for_ET_staff2)

xmlstr_2 = minidom.parseString(ET.tostring(part_et_2)).toprettyxml(indent="   ")

#to delete <?xml version="1.0"　?> in line 1
xmlstr_2 = xmlstr_2[23:]            

#read template.xml to prepare part_et XML data and generate the whole XML
wholeXML_staff2_text = ""
with open("./bfaaap/yoloToxml/template.xml", 'r') as f:
    template_text = f.read()
    wholeXML_staff2_text = template_text +'\n' + xmlstr_2 +'\n</score-partwise>'

#save the resulting xml in ./xml/ directory
FILE_DIR_PATH
new_dir_path = FILE_DIR_PATH + '/xml'
os.makedirs(new_dir_path, exist_ok=True)
new_xml_filepath = new_dir_path + '/' + FILE_BASENAME_WITHOUTEXT + '_staff2.xml'
with open(new_xml_filepath, 'w') as f:
    f.write(wholeXML_staff2_text)
