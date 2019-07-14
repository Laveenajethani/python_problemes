#python code for alarm
from pygame import mixer
import time
def sound():
    mixer.init()
    mixer.music.load('C:\Users\LAVEENA\Downloads\alarm_alarm_alarm.mp3')
def alarm():
    hor=int(raw_input('enter the hour-'))
    minn=int(raw_input('enter the min'))
    sec=int(raw_input('enter the sec-'))
    while True:
            if time.localtime().tm_hour==hor and time.localtime().tm_min==minn and time.localtime().tm_sec==sec:
                print("wake up")
                break
    while n>0:
            mixer.music.play()
            time.sleep()
    sn=str(raw_input('press s snoze'))
    if sn=='s':
            n=3
            time.sleep(100)
            while n>0:
               mixer.music.play()
               time.sleep(2)
    else:
            exit()
