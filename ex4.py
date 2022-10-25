import os
"""
Exercise 4: Create a script which can change the
stereo audio into mono output and the
opposite, depending on the input file
"""

def mono_stereo():
    var = input("Escriu mono o stereo depenent de com vols que estigui el video: ")

    if var == "mono":
        c4 = "ffmpeg -i bbb_cut.mp4 -ac 1 mono.mp4"

    elif var == "stereo":
        c4 = "ffmpeg -i bbb_cut.mp4 -ac 2 stereo.mp4"

    os.system(c4)

