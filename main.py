import os
import random
from threading import Thread
from time import sleep

from termcolor import colored
from playsound import playsound
import pygame
from config import *

# Importing module specified in the config file
art = __import__(f'arts.{artFile}', globals(), locals(), ['*'])



def replaceMultiple(mainString, toBeReplace, newString):
    for elem in toBeReplace:
        if elem in mainString:
            mainString = mainString.replace(elem, newString)
    return mainString


def pprint(art, time):
    color_used = [random.choice(color)]
    colorAttribute = []
    for i in range(len(art)):
        if art[i] in colorCodes:
            if art[i] == '⑨':
                colorAttribute = [colorCodes[art[i]]]
            elif art[i] == '⑩':
                colorAttribute = []
            elif art[i] == '®':
                color_used = color
            else:
                color_used = [colorCodes[art[i]]]

        print(
            colored(replaceMultiple(art[i], colorCodes, ''), random.choice(color_used), attrs=colorAttribute),
            sep='', end='', flush=True)
        sleep(time)

# this is fo music 
def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


# Print the code before wishing
def pcode():
    if codePrint:
        for i in range(len(art.code)):
            print(colored(art.code[i], codeColor), sep='', end='', flush=True)
            sleep(codingSpeed)
        input('\n\n' + colored('python3', 'blue') + colored(' PyBirthdayWish.py', 'yellow'))
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        input(colored('press {Enter} and turn up volume to max', 'blue'))
        os.system('cls' if os.name == 'nt' else 'clear')


# Clearing terminal
os.system('cls' if os.name == 'nt' else 'clear')
pcode()

# Provide the file path of the audio file
file_path = 'HappyBirthday.mp3'

# Start the audio playback in a separate thread
audio_thread = Thread(target=play_audio, args=(file_path,))
audio_thread.start()

# Start printing the art in a separate thread
print_thread = Thread(target=pprint, args=(art.mainArt, speed))
print_thread.start()

# Wait for both threads to finish
audio_thread.join()
print_thread.join()
