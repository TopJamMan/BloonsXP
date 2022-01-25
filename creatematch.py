import pyautogui
from placetowers import *
from creatematch import *

scroll_pos = (1750, 550)

def create_match():
    # PLAY
    pyautogui.click(x=850, y=900, interval=0.1)
    # EXPERT
    pyautogui.click(x=1350, y=1000, interval=0.1)
    # INFERNAL
    pyautogui.click(x=550, y=600, interval=0.1)
    # EASY
    pyautogui.click(x=630, y=430, interval=0.2)
    # DEFLATION
    pyautogui.click(x=1250, y=450, interval=3)
    # OK
    pyautogui.click(x=950, y=750, interval=0.5)
    monkey_village(scroll_pos)
    sniper_monkey(scroll_pos)
    alchemist()
    
    #Play button
    pyautogui.click(x=1800, y=1000, clicks=2, interval=0.1)
    pyautogui.click(x=960, y=540)
