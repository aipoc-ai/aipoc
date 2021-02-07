import subprocess
import sys
from time import sleep

def write_query(query):
    file1 = open("AIPOC/AIPOC/features/play_music/audio_query.txt","r+")
    file1.truncate(0)
    file1.close()
    with open('AIPOC/AIPOC/features/play_music/audio_query.txt','w') as fb:
        fb.write(query)

def play_music_func(query):
            
    write_query(query)



    cmd = 'python3 AIPOC/AIPOC/features/play_music/play_spotify.py'

    p= subprocess.Popen(cmd,shell=True)
    return p