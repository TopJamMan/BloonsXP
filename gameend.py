import pyautogui
import time
from creatematch import *

def game_end(running):
    while(running == True):
        time.sleep(1)
        print(pyautogui.pixelMatchesColor(960, 540, (60, 96, 145)))

        if(pyautogui.pixelMatchesColor(960, 540, (60, 96, 145))):
            running = False
            print('Game ended. Restarting.')
            pyautogui.click(x=950, y=900, interval=0.1)
            pyautogui.click(x=700, y=850, interval=0.1)
            create_match()
