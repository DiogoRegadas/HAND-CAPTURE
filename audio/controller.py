from pydub import AudioSegment
from pydub.playback import play
import pygame

import threading

AudioSegment.converter = 'C:/Users/User/Documents/ffmpeg-7.1.1-essentials_build/bin/ffmpeg.exe'

music = AudioSegment.from_file("C:/Users/User/Documents/HandCapture/HandCapture/src/audio/Billie Eilish - WILDFLOWER (BILLIE BY FINNEAS).wav")

def volume(vol):
    volume = min(max(round(vol / 100, 2), 0.0), 1.0)
    print('VOLUME:' + str(volume))

    pygame.mixer.music.set_volume(volume)

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/User/Documents/HandCapture/HandCapture/src/audio/Billie Eilish - WILDFLOWER (BILLIE BY FINNEAS).wav")
    pygame.mixer.music.play(loops=-1)

