from pydub import AudioSegment
from pychorus.helpers import find_and_output_chorus
from pydub import AudioSegment
import random, os
from subprocess import call
forappending = []
mixappends = []
# rando = ['0.03', 'scratch05.mp3','']
effects = ['scratch03.mp3', 'scratch05.mp3', 'scratch10.mp3','effect1.mp3','effect2.mp3','effect3.mp3', 'Kill_Bill_Siren_SFX.mp3','siren-hall.mp3','soundmix.mp3',
    'beep-sound.mp3', 'beep.mp3', 'air-horn-djmix-1.mp3', 'Laser_dancehall.mp3']
import os, glob
path = r"C:\Users\Kariuki\Documents\Python\Audio\Categorized"
filesindir=[]
finishedfiles = []
# allfiles = os.listdir(path)
g = glob.glob(path+'\*.wav')
# print(g)
for f in g:
    filesindir.append(f)
remainder = len(forappending)%2
while filesindir != 0:
    for file in filesindir:
        remainder = len(forappending)%2
        if remainder == 0:
            AUDIO_FILE1 = filesindir[0]
            slash = path + '\\'
            AUDIO_FILE_EXTENSION1 = AUDIO_FILE1.replace(slash,'')  
            print(AUDIO_FILE_EXTENSION1)
            sound1 = AudioSegment.from_file(filesindir[0])
            r = random.choice(effects)
            random_effect = AudioSegment.from_file(r)
            halfway_point1 = len(sound1) // 2
            print( random_effect)
            print(halfway_point1)
            if halfway_point1 > 105357:
                halfway_point1 = len(sound1) // 4
                x = range(0,int(halfway_point1))
                print(x)
                rtime = random.choice(x)
                first_half1 = sound1.overlay(random_effect, position=rtime, gain_during_overlay=-2, times=1)
                first_half11 = sound1[:halfway_point1]
                first_half11.export(AUDIO_FILE_EXTENSION1, format="mp3")
            elif halfway_point1 > 145357:
                halfway_point1 = len(sound1) // 5
                x = range(0,int(halfway_point1))
                print(x)
                rtime = random.choice(x)
                first_half1 = sound1.overlay(random_effect, position=rtime, gain_during_overlay=-2, times=1)
                first_half11 = sound1[:halfway_point1]
                first_half11.export(AUDIO_FILE_EXTENSION1, format="mp3")
            else:
                halfway_point1 = len(sound1) // 2
                x = range(0,int(halfway_point1))
                print(x)
                rtime = random.choice(x)
                first_half1 = sound1.overlay(random_effect, position=rtime, gain_during_overlay=-2, times=1)
                first_half11 = sound1[:halfway_point1]
                first_half11.export(AUDIO_FILE_EXTENSION1, format="mp3")

            AUDIO_FILE2 =  filesindir[1]
            slash = path + '\\'
            AUDIO_FILE_EXTENSION2 = AUDIO_FILE2.replace(slash,'') 
            print(AUDIO_FILE_EXTENSION2)
            sound2 = AudioSegment.from_file(filesindir[1])
            # from spleeter.separator import Separator
            # output = 'audio_output'
            # input = AUDIO_FILE_EXTENSION2
            # # Using embedded configuration.
            # separator = Separator('spleeter:2stems')
            # separator.separate_to_file(input, output)
            # from subprocess import call
            # call(['spleeter', 'separate', '-o', 'audio_output', AUDIO_FILE_EXTENSION2])
            # sound2 = AudioSegment.from_file(AUDIO_FILE_EXTENSION2)
            beginning_part_time = sound2[1000:12000]
            beginning_var = "beginning.mp3"
            beginning_part_time.export(beginning_var, format="mp3")
            beginning_part_audio = AudioSegment.from_file("beginning.mp3")
            main_scratch = AudioSegment.from_file("main scratch.mp3")
            beginning_part_output = beginning_part_audio.append(main_scratch, crossfade=0)
            beginning_part_output.export(beginning_var, format='mp3')
            beginning_part_audio = AudioSegment.from_file("beginning.mp3")

            
            position =  len(first_half11)-12000
            # beginning_part_audio2 = AudioSegment.from_file("beginning.mp3")
            output = first_half11.overlay(beginning_part_audio, position=position,gain_during_overlay=-2)
            # export
            individual_mix_name = AUDIO_FILE_EXTENSION1
            output.export(individual_mix_name, format='mp3')
            # append mix
        
            forappending.append(individual_mix_name)
            print(forappending)
            list_length = len(forappending)
            print("The length of the list is {}".format(list_length))
            if list_length == 2: #input 4 songs only
                audiotoappend1 = AudioSegment.from_file(forappending[0])
                audiotoappend2 = AudioSegment.from_file(forappending[1])
                output = audiotoappend1.append(audiotoappend2, crossfade=0)
                export_name = 'appended.mp3'
                output.export(export_name, format='mp3')
                mixappends.append(export_name)
                print('4 song mix is {}'.format(export_name))
                print('The appended is {}'.format(mixappends))
                # forappending.pop(0)
                # forappending.pop(1)
            elif list_length > 2: #input more than 4 songs
                recent_mix = AudioSegment.from_file(forappending[-1])
                recent_appended = AudioSegment.from_file(mixappends[-1])
                recent_output = recent_appended.append(recent_mix, crossfade=0)
                export_name = 'appended.mp3'
                recent_output.export(export_name, format='mp3')
                
            else:
                print('Name is {}'.format(individual_mix_name))
            filesindir.pop(0)

        else:
            AUDIO_FILE1 = filesindir[0]
            slash = path + '\\'
            AUDIO_FILE_EXTENSION1 = AUDIO_FILE1.replace(slash,'')  
            print(AUDIO_FILE_EXTENSION1)
            sound1 = AudioSegment.from_file(filesindir[0])
            r = random.choice(effects)
            random_effect = AudioSegment.from_file(r)
            halfway_point1 = len(sound1) // 2
            print( random_effect)
            print(halfway_point1)
            if halfway_point1 > 105357:
                halfway_point1 = len(sound1) // 4
                x = range(0,int(halfway_point1))
                print(x)
                rtime = random.choice(x)
                first_half1 = sound1.overlay(random_effect, position=rtime, gain_during_overlay=-2, times=1)
                first_half11 = sound1[:halfway_point1]
                first_half11.export(AUDIO_FILE_EXTENSION1, format="mp3")
            elif halfway_point1 > 145357:
                halfway_point1 = len(sound1) // 5
                x = range(0,int(halfway_point1))
                print(x)
                rtime = random.choice(x)
                first_half1 = sound1.overlay(random_effect, position=rtime, gain_during_overlay=-2, times=1)
                first_half11 = sound1[:halfway_point1]
                first_half11.export(AUDIO_FILE_EXTENSION1, format="mp3")
            else:
                halfway_point1 = len(sound1) // 2
                x = range(0,int(halfway_point1))
                print(x)
                rtime = random.choice(x)
                first_half1 = sound1.overlay(random_effect, position=rtime, gain_during_overlay=-2, times=1)
                first_half11 = sound1[:halfway_point1]
                first_half11.export(AUDIO_FILE_EXTENSION1, format="mp3")
            
            
            AUDIO_FILE2 =  filesindir[1]
            slash = path + '\\'
            AUDIO_FILE_EXTENSION2 = AUDIO_FILE2.replace(slash,'') 
            print(AUDIO_FILE_EXTENSION2)
            sound2 = AudioSegment.from_file(filesindir[1])
            print(sound2)
            halfway_point2 = len(sound2) // 2
            # rtime2 = halfway_point2 - 30000
            rtime2 = 3000
            print(rtime2)
            scratch2 = AudioSegment.from_file('scratch03.mp3')
            first_half2 = sound2.overlay(scratch2, position=rtime2, gain_during_overlay=-7, times=2)
            first_half22 = first_half2[:halfway_point2]
            first_half22.export(AUDIO_FILE_EXTENSION2, format="mp3")

            # Split song
            from subprocess import call
            # AUDIO_FILE1  = AUDIO_FILE1
            # call(['spleeter', 'separate', '-o', 'audio_output', AUDIO_FILE1])
            call(['spleeter', 'separate', '-o', 'audio_output', AUDIO_FILE_EXTENSION2])
            input1 = AUDIO_FILE_EXTENSION2
            AUDIO_FILE2_remove_mp3 = AUDIO_FILE_EXTENSION2.replace('.wav','')
            output = r"audio_output\%s\chorus.wav"%AUDIO_FILE2_remove_mp3
            chorus_start_sec = find_and_output_chorus(input_file=input1,output_file=output, clip_length=30)
            # overlay 2 songs
            x = random.choice(r'audio_output\%s'%AUDIO_FILE2_remove_mp3)
            # Accompaniment = r'audio_output\%s\accompaniment.wav'%AUDIO_FILE2
            Accompaniment = r'audio_output\%s'%AUDIO_FILE2_remove_mp3
            random_file=random.choice(os.listdir(Accompaniment))
            random_file2 = Accompaniment+"\{}".format(random_file)
            print(random_file2)
            accompaniment = AudioSegment.from_file(random_file2)
                # mix sound 1 and 2 after 10000ms into
            position =  len(first_half11)//1.3
            output = first_half11.overlay(accompaniment, position=position,gain_during_overlay=-2)
            # export
            individual_mix_name = AUDIO_FILE_EXTENSION1
            output.export(individual_mix_name, format='mp3')
            # append mix
            
            forappending.append(individual_mix_name)
            print(forappending)
            list_length = len(forappending)
            print("The length of the list is {}".format(list_length))
            if list_length == 2: #input 4 songs only
                audiotoappend1 = AudioSegment.from_file(forappending[0])
                audiotoappend2 = AudioSegment.from_file(forappending[1])
                output = audiotoappend1.append(audiotoappend2, crossfade=0)
                export_name = 'appended.mp3'
                output.export(export_name, format='mp3')
                mixappends.append(export_name)
                print('4 song mix is {}'.format(export_name))
                print('The appended is {}'.format(mixappends))
                # forappending.pop(0)
                # forappending.pop(1)
            elif list_length > 2: #input more than 4 songs
                recent_mix = AudioSegment.from_file(forappending[-1])
                recent_appended = AudioSegment.from_file(mixappends[-1])
                recent_output = recent_appended.append(recent_mix, crossfade=0)
                export_name = 'appended.mp3'
                recent_output.export(export_name, format='mp3')
                
            else:
                print('Name is {}'.format(individual_mix_name))
            filesindir.pop(0)
else: 
    print("Done")