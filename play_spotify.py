import vlc 
from time import sleep
import pafy 
from search_youtube import search
from main_program import command,speak

query = command() 

url = search(str(query))
  
 
video = pafy.new(url) 
  
 
best = video.getbest() 
  
 
media = vlc.MediaPlayer(best.url) 
  

media.play() 


sleep(5)
while media.is_playing():
     sleep(1)
     x = command()
     if x=="stop":
          break

      