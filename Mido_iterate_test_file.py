import pygame
import mido
import threading
from mido import MidiFile

# threading.Thread()

# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load("HesaPirate.mid")
# pygame.mixer.music.play()
# input("no")

mid = MidiFile("HesaPirate.mid")
for msg in mid.play():
    print(msg.type)