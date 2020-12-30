import subprocess
import sys
from time import sleep

def write_query(query):
    file1 = open("audio_query.txt","r+")
    file1.truncate(0)
    file1.close()
    with open('audio_query.txt','w') as fb:
        fb.write(query)

def play_music_func(query):
            
    write_query(query)



    cmd = 'python3 play_spotify.py'

    p= subprocess.Popen(cmd,shell=True)
    return p
