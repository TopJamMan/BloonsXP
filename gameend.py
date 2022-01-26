import pyautogui
import time
import creatematch
from datetime import datetime

def game_end(running, successful_runs):
    while(running == True):
        time.sleep(1)

        if(pyautogui.pixelMatchesColor(960, 540, (60, 96, 145))):
            running = False
            #end_time = start_time - datetime.now()
            successful_runs += 1
            print('Game ended. Restarting.')
            #print('This game took: =', end_time.strftime('%M:%S'))
            print('Total successful runs:', successful_runs)
            pyautogui.click(x=950, y=900, interval=0.5)
            pyautogui.click(x=700, y=850, interval=3)
            creatematch.create_match(successful_runs)
