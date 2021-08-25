import load2

import xml.etree.ElementTree as ET
from bfaaap.yoloToxml.yoloToxml import musicData2XML
from xml.dom import minidom

#here, provide a FILE_PATH for a sheet music image (either .jpg or .png)
FILE_PATH ='./static/test1.png'
#input base data for sheet music of interest:
tempo = 120 #
fifths = -1 #if the key signature after clef has three #, the number is 3 (positive integer); if the key signature has one b, the number is -1 (negative integer); if the key signature does't have any of them, the number is 0
beats = 3 #if the beat is 3/4, the "beats" is 3 and the "beat_type" is 4. 
beat_type = 2 #see the above
preset_measure_duration = 1024 * beats / beat_type #

conv_img = load2.convImage(FILE_PATH=FILE_PATH, tempo=tempo, fifths=fifths, beats=beats, beat_type=beat_type, preset_measure_duration=preset_measure_duration)

conv_img.level_original_img()
conv_img.detect_bar()
conv_img.show_staff_img()
conv_img.generate_xml()


# part_et = ET.Element('part')
# part_et.attrib = {'id':'P1'}

# # dict example
# dict_sample_1 = {'part': {'measure1': {'attrib': {'number': '1', 'width': '360'}, 'attributes': {'divisions': '256', 'key': {'fifths': '-1', 'mode': 'major'}, 'time': {'beats': '3', 'beat-type': '2'}, 'staves': '1', 'clef': {'sign': 'G', 'line': '2'}}, 'note1': {'pitch': {'step': 'A', 'octave': '3'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note2': {'chord': '', 'pitch': {'step': 'D', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note3': {'chord': '', 'pitch': {'step': 'F', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note4': {'pitch': {'step': 'A', 'octave': '3'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note5': {'chord': '', 'pitch': {'step': 'D', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note6': {'chord': '', 'pitch': {'step': 'F', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note7': {'rest': '', 'duration': '256', 'voice': '1', 'type': 'quarter', 'staff': '1'}, 'note8': {'pitch': {'step': 'E', 'octave': '4'}, 'duration': '256', 'voice': '1', 'type': 'quarter', 'stem': 'up', 'staff': '1'}, 'note9': {'chord': '', 'pitch': {'step': 'G', 'octave': '4'}, 'duration': '256', 'voice': '1', 'type': 'quarter', 'stem': 'up', 'staff': '1'}}, 'measure2': {'attrib': {'number': '2', 'width': '360'}, 'note1': {'pitch': {'step': 'A', 'octave': '3'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note2': {'chord': '', 'pitch': {'step': 'C', 'alter': '1', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note3': {'chord': '', 'pitch': {'step': 'E', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note4': {'pitch': {'step': 'A', 'octave': '3'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note5': {'chord': '', 'pitch': {'step': 'C', 'alter': '1', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note6': {'chord': '', 'pitch': {'step': 'E', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note7': {'rest': '', 'duration': '512', 'voice': '1', 'type': 'half', 'staff': '1'}}, 'measure3': {'attrib': {'number': '3', 'width': '360'}, 'note1': {'pitch': {'step': 'C', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note2': {'chord': '', 'pitch': {'step': 'F', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note3': {'chord': '', 'pitch': {'step': 'A', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note4': {'pitch': {'step': 'C', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'up', 'staff': '1'}, 'note5': {'chord': '', 'pitch': {'step': 'F', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'up', 'staff': '1'}, 'note6': {'chord': '', 'pitch': {'step': 'A', 'octave': '4'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'up', 'staff': '1'}, 'note7': {'rest': '', 'duration': '256', 'voice': '1', 'type': 'quarter', 'staff': '1'}, 'note8': {'pitch': {'step': 'G', 'octave': '4'}, 'duration': '256', 'voice': '1', 'type': 'quarter', 'stem': 'up', 'staff': '1'}, 'note9': {'chord': '', 'pitch': {'step': 'B', 'alter': '-1', 'octave': '4'}, 'duration': '256', 'voice': '1', 'type': 'quarter', 'stem': 'up', 'staff': '1'}} }}

# dict_sample_2 = {'part': {'measure1': {'attrib': {'number': '1', 'width': '360'}, 'attributes': {'divisions': '256', 'key': {'fifths': '-1', 'mode': 'major'}, 'time': {'beats': '3', 'beat-type': '2'}, 'staves': '1', 'clef': {'sign': 'F', 'line': '4'}}, 'note1': {'pitch': {'step': 'D', 'octave': '3'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note2': {'pitch': {'step': 'C', 'octave': '2'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'up', 'staff': '1'}, 'note3': {'rest': '', 'duration': '512', 'voice': '1', 'type': 'half', 'staff': '1'}}, 'measure2': {'attrib': {'number': '2', 'width': '360'}, 'note1': {'pitch': {'step': 'A', 'octave': '2'}, 'duration': '768', 'voice': '1', 'type': 'half', 'dot': '', 'stem': 'up', 'staff': '1'}, 'note2': {'pitch': {'step': 'B', 'alter': '-1', 'octave': '2'}, 'duration': '256', 'voice': '1', 'type': 'quarter', 'stem': 'up', 'staff': '1'}, 'note3': {'pitch': {'step': 'A', 'octave': '2'}, 'duration': '256', 'voice': '1', 'type': 'quarter', 'stem': 'up', 'staff': '1'}, 'note4': {'pitch': {'step': 'F', 'octave': '2'}, 'duration': '256', 'voice': '1', 'type': 'quarter', 'stem': 'up', 'staff': '1'}}, 'measure3': {'attrib': {'number': '3', 'width': '360'}, 'note1': {'pitch': {'step': 'F', 'octave': '2'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note2': {'chord': '', 'pitch': {'step': 'F', 'octave': '3'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'up', 'staff': '1'}, 'note3': {'pitch': {'step': 'F', 'octave': '2'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'down', 'staff': '1'}, 'note4': {'chord': '', 'pitch': {'step': 'F', 'octave': '3'}, 'duration': '512', 'voice': '1', 'type': 'half', 'stem': 'up', 'staff': '1'}, 'note5': {'rest': '', 'duration': '512', 'voice': '1', 'type': 'half', 'staff': '1'}} }}
# part_et_1 = musicData2XML(part_et, dict_sample_1, dict_sample_2)

# xmlstr_1 = minidom.parseString(ET.tostring(part_et_1)).toprettyxml(indent="   ")

# #to delete <?xml version="1.0"　?> in line 1
# xmlstr_1 = xmlstr_1[23:]            

# #read template.xml to prepare part_et XML data and generate the whole XML
# wholeXML_staff2_text = ""
# with open("./bfaaap/yoloToxml/template.xml", 'r') as f:
#     template_text = f.read()
#     wholeXML_staff2_text = template_text +'\n' + xmlstr_1 +'\n</score-partwise>'

# print(wholeXML_staff2_text)