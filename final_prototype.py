from gpiozero import Button
import paralleldots
import os
from picamera import PiCamera
import sys

from signal import pause
from time import sleep


import RPi.GPIO as GPIO

import pygame
from playsound import playsound
pygame.init()



GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

buzzer = 23
GPIO.setup(buzzer,GPIO.OUT)
camera = PiCamera()
    
pins = {
  "buzzer":23
  }


#Declares duration of the dot and dash to be used in sleep method
dotdur=0.2
dashdur=dotdur*3

GPIO.setmode(GPIO.BCM) #Sets GPIO board to Broadcom
GPIO.setwarnings(False) #Debugg mode toggle
GPIO.setup(pins["buzzer"],GPIO.OUT) #Sets up GPIO channels declared above as output.


#Text to morse code dictionary reference. First list is text, sub-list is string of that characters dot/dash sequence.
ref = {' ': ' ', "'": '.----.', '(': '-.--.-', ')': '-.--.-', ',': '--..--', '-': '-....-', '.': '.-.-.-', '/': '-..-.', 
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
        '8': '---..', '9': '----.', ':': '---...', ';': '-.-.-.', '?': '..--..', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', '_': '..--.-'}

#dot function
def dot(char):
    print(" .") #morse feedback to terminal
    GPIO.output(pins["buzzer"],GPIO.HIGH)
    sleep(dotdur)#waits dot duration value in seconds
    GPIO.output(pins["buzzer"],GPIO.LOW)
    sleep(dotdur)#waits, then next iteration
    
#dash function. Has " functions.
def dash(char):
    print(" _")
    GPIO.output(pins["buzzer"],GPIO.HIGH)
    sleep(dashdur)#waits dot duration value in seconds
    GPIO.output(pins["buzzer"],GPIO.LOW)
    sleep(dotdur)
    
# text to morse code function
def CODE(data):
    try:
        for char in data:
            print ('\033[1m'+char.upper()+'\033[0m')#Text feedback to terminal. Bolds, then resets.
            for symbol in ref[char.upper()]:
                if symbol == ".":
                    dot(char)
                elif symbol == "-":
                    dash(char)
                else:
                    sleep(0.5)
    except Exception as e:
        print(e)

print("\033[1m"+"\nMorsePi"+"\033[0m")


def take_picture_with_camera():
    paralleldots.set_api_key("br13ubwK9UvtgVahL09oDrw2KxLtRGKygrgonAmLqjY")
    paralleldots.get_api_key()
    camera.start_preview()
    #camera.rotation(180)
    sleep(0.5)
    
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    path = "/home/pi/Desktop/image.jpg"
    s = (paralleldots.facial_emotion(path))
    ans = dict(s)

    if("facial_emotion" in ans):
        a = list(ans['facial_emotion'])
        b = dict(a[0])
        emotions = b['tag']
        #while True:
        print(emotions)
        if(emotions == "Angry"):
            pygame.mixer.music.load("/home/pi/Sounds/Angry.mp3")
            pygame.mixer.music.play()
        else:
            if(emotions == "Disgust"):
                pygame.mixer.music.load("/home/pi/Sounds/Disgust.mp3")
                pygame.mixer.music.play()
            else:
               if(emotions == "Fear"):
                   pygame.mixer.music.load("/home/pi/Sounds/Fear.mp3")
                   pygame.mixer.music.play()
               else:
                   if(emotions == "Happy"):
                       pygame.mixer.music.load("/home/pi/Sounds/Happy.mp3")
                       pygame.mixer.music.play()    
                   else:
                       if(emotions == "Neutral"):
                           pygame.mixer.music.load("/home/pi/Sounds/Normal.mp3")
                           pygame.mixer.music.play()
                       else:
                           if(emotions == "Normal"):
                               pygame.mixer.music.load("/home/pi/Sounds/Normal.mp3")
                               pygame.mixer.music.play()    
                           else:
                               if(emotions == "Sad"):
                                   pygame.mixer.music.load("/home/pi/Sounds/Sad.mp3")
                                   pygame.mixer.music.play()    
                               else:
                                   if(emotions == "Surprise"):
                                       pygame.mixer.music.load("/home/pi/Sounds/Surprise.mp3")
                                       pygame.mixer.music.play()    
        if(emotions == "Neutral"):
            CODE("Normal")
        CODE(emotions) # morse code for the emotions
    else:
        print("Face is not detected clearly :( ")
        GPIO.output(buzzer, GPIO.HIGH)
        sleep(1)
        GPIO.output(buzzer,GPIO.LOW)
        # Play NoFace
        pygame.mixer.music.load("/home/pi/Sounds/NoFace.mp3")
        pygame.mixer.music.play() 
        CODE("No Face")
        #os.execv('/home/pi/button.py', sys.argv)
    


button = Button(4)
button.when_pressed = take_picture_with_camera
 

