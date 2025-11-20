# main.py
from detection.detector import detect_hand
from video.capture import capture_vd
from detection.detector import detect_hand
from utilis.monitor import start_monitoring
from audio.controller import play_music

def dummy_callback(frame):
    print(123)# Just pass or print something if you want
    pass


def main():
    #start monitoring pc cpu % and memory usage
    #start_monitoring()
    # Start video capture and send each frame to the detection function
    play_music()
    capture_vd()

if __name__ == "__main__":
    main()

