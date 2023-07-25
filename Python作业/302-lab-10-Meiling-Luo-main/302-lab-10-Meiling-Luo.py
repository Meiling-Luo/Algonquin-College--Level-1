
from gtts import gTTS
from pygame import mixer
import time




d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot',
     'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
     'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec',
     'r': 'romeo', 's': 'sierra', 't': 'tango', 'u': 'uniform',
     'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'}

name = 'Meiling Luo'

def stringToICAO(letter):
    listOfLetter = list(letter.lower())
    for eachLetter in listOfLetter:
        if " " == eachLetter:
            listOfLetter.remove(eachLetter) 
    listOfNewLetter = []
    for item in listOfLetter:
        listOfNewLetter.append(d[item])
    print(listOfNewLetter)
    return letter + str(listOfNewLetter)


myname = gTTS(text=stringToICAO(name), lang='en')
myname.save("Myname.mp3")




# Play the audio
mixer.init()
mixer.music.load("Result.mp3")
mixer.music.play()
# Wait for the audio to be played
time.sleep(15)