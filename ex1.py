import os
"""
Exercise 1: Create a script which can cut N seconds the BBB video. That N seconds will be read
from user input.
"""

def cut():
    inp = int(input('Entra el numero de segons que vols que duri el video: '))
    N = inp
    # cut the video from 0 to N seconds.
    c1 = "ffmpeg -i bbb.mp4 -ss 00:00:00 -t 00:00:{0} bbb_cut.mp4".format(N)
    os.system(c1)
