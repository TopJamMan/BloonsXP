import pyautogui
import time
import sys
from creatematch import *
from gameend import *

pyautogui.click(x=960, y=1)
running = False

create_match()
running = True
pyautogui.moveTo(10, 10)
game_end(running)
