import os
"""
Exercise 3: Create a script which can resize the BBB
video into 4 differents video outputs.
"""

def resize():

    inp = int(input('Tria quina resolució vols pel video (escriu 1,2,3,4) '
                '\n1. 720p  \n2. 420p \n3.360x240 \n4.160x120'))

    print(inp)

    if inp == 1:
        c3 = "ffmpeg -i bbb_cut.mp4 -s hd720 -c:a copy bbb_720p.mp4"
    elif inp == 2:
        c3 = "ffmpeg -i bbb_cut.mp4 -s hd480 -c:a copy bbb_480p.mp4"
    elif inp == 3:
        c3 = "ffmpeg -i bbb_cut.mp4 -s 360x240 -c:a copy bbb_360x240.mp4"
    elif inp == 4:
        c3 = "ffmpeg -i bbb_cut.mp4 -s 160x120 -c:a copy bbb_160x120.mp4"


    os.system(c3)