import os
from playsound import playsound
import time
from pygame import mixer
import enumerare
from mutagen.mp3 import MP3
timp = 0
n = 0
k = 0
ora = 45
pauza = 10
j = 0

mixer.init()
# folder path

print(enumerare.count, "fisiere")
run = True
i = 1
k = 0
for i in range(enumerare.count + 1):
    while i:
            time.sleep(1) # se verifica valorile la fiecare 6 secunde
            now = time.gmtime()
            print("acesta este i: ", i)
            timp = 0
            print("timpul dinafara loopului", timp)
            if (now[3]  == 5 + i):
                if (now[3] == 17):
                    if (now[4] == 00 or now[4] == 55):
                            for j in range(2):
                                print("j este :", j)
                                print("acesta este k:", k)
                                audio = MP3(f'Music/{j+k}.mp3')
                                print("sa inceapa muzica")
                                pauza = int(audio.info.length)
                                mixer.music.load(f'Music/{j + k }.mp3')
                                mixer.music.play()
                                time.sleep(pauza)
                                timp += int(audio.info.length)
                                print("acesta este timpul redat in enumerare:", timp)
                                n += 1
                                if (timp < 460 and n == 2):
                                    print("test timp mai mic n=2")
                                    mixer.music.load(f'Music/{j + k + 1}.mp3')
                                    mixer.music.play()
                                    time.sleep(600 - timp)
                                    print(i)
                                    k += 1
                                elif(timp > 610 and n == 1):
                                    print("test timp > n = 1")
                                    print("NU ESTRE BINE ABSOLUT DELOC TE ROG INCETEAZA!!!!!!!")
                                    mixer.music.load(f'Music/{j + k + 1}.mp3')
                                    mixer.music.play()
                                    time.sleep(600 - timp)
                                    k += 1
                if(now[4] == 45 - ( i * 5 ) ) :
                        for j in range(2):
                            print("j este :", j)
                            print("acesta este k:",k)
                            audio = MP3(f'Music/{j+k}.mp3')
                            print("sa inceapa muzica")
                            pauza = int(audio.info.length)
                            mixer.music.load(f'Music/{j + k }.mp3')
                            mixer.music.play()
                            time.sleep(pauza)
                            timp += int(audio.info.length)
                            print("acesta este timpul redat in enumerare:", timp)
                            n += 1
                            if (timp < 460 and n == 2):
                                print("test timp mai mic n=2")
                                mixer.music.load(f'Music/{j + k + 1}.mp3')
                                mixer.music.play()
                                time.sleep(600 - timp)
                                print(i)
                                k += 1
                            elif(timp > 610 and n == 1):
                                    print("test timp > n = 1")
                                    print("NU ESTRE BINE ABSOLUT DELOC TE ROG INCETEAZA!!!!!!!")
                                    time.sleep(timp - 600)
                        k += 2
                        i = 0
