import os
from pydub import AudioSegment
import googleCloud
from difflib import SequenceMatcher

# files
# Mode to be set

    
files = os.listdir('audioWav')
count = 0
for file in files[28:54]:
    if count <= 12:
        with open('text_file.txt', 'w') as f:
            runThis = googleCloud.sample_recognize(('audioWav/' + file), 'en-IN')
            quoteThis = "please call stella ask her to bring these things with her from the store six spoons of fresh snow peas five thick slabs of blue cheese and maybe a snack for her brother bob we also need a small plastic snake and big toy frog for the kids she can scoop these things into three red bags and we will go meet her wednesday at the train station"
            quoteThis = quoteThis[0:len(runThis)]
            f.write(str(runThis))
            print(runThis)
            s = SequenceMatcher(None, quoteThis, runThis)
            print(s.ratio())
        count+=1
    