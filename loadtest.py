from flask.scaffold import F
import load2

#here, provide a FILE_PATH for a sheet music image (either .jpg or .png)
FILE_PATH ='./static/test.jpg'
#input base data for sheet music of interest:
tempo = 120 #
fifths = -1 #if the key signature after clef has three #, the number is 3 (positive integer); if the key signature has one b, the number is -1 (negative integer); if the key signature does't have any of them, the number is 0
beats = 3 #if the beat is 3/4, the "beats" is 3 and the "beat_type" is 4. 
beat_type = 2 #see the above
preset_measure_duration = 1024 * beats / beat_type #

conv_img = load2.conv_image(FILE_PATH=FILE_PATH, tempo=tempo, fifths=fifths, beats=beats, beat_type=beat_type, preset_measure_duration=preset_measure_duration)

conv_img.level_original_img()

