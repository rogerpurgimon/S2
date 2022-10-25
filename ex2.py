import os
"""Exercise 2: Create a script which will extract the YUV
histogram from the previous BBB video you’ve
done and create a new video with both images
at the same time.
"""

def histogram():
    # Due problems with the 0:1 channel it is inserted "-c:a copy".
    s = "split=2[a][b],[b]histogram,format=yuv420p[hh],[a][hh]overlay"
    c2 = "ffmpeg -i bbb_cut.mp4 -vf {0} -c:a copy bbbhistogram.mp4".format(s)
    os.system(c2)
