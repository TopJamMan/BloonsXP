import pyautogui
import time
import creatematch

def game_end(running):
    while(running == True):
        time.sleep(1)

        if(pyautogui.pixelMatchesColor(960, 540, (60, 96, 145))):
            running = False
            print('Game ended. Restarting.')
            pyautogui.click(x=950, y=900, interval=0.5)
            pyautogui.click(x=700, y=850, interval=3)
            creatematch.create_match()
