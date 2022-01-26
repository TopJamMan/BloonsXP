import pyautogui

def monkey_village(scroll_pos):
    # Scroll to position
    pyautogui.moveTo(scroll_pos[0], scroll_pos[1])
    for i in range(0, 11):
        pyautogui.scroll(-1)

    # Select and place Monkey Village (Opens upgrade window)
    pyautogui.click(x=1700, y=900)
    pyautogui.click(x=1575, y=660, clicks=2, interval=0.1)

    # Upgrade Monkey Village
    pyautogui.click(x=330, y=500, clicks=2, interval=0.1)
    pyautogui.click(x=330, y=800, clicks=2, interval=0.1)

def sniper_monkey(scroll_pos):
    # Scroll to position
    pyautogui.moveTo(scroll_pos[0], scroll_pos[1])
    for i in range(0, 4):
        pyautogui.scroll(1)

    # Select and place Sniper Monkey (Opens upgrade window)
    pyautogui.click(x=1800, y=200)
    pyautogui.click(x=1600, y=500, clicks=2, interval=0.1)

    # Upgrade Sniper Monkey
    pyautogui.click(x=330, y=650, clicks=2, interval=0.1)
    pyautogui.click(x=330, y=800, clicks=4, interval=0.1)

def alchemist():
    # Select and place Alchemist (Opens upgrade window)
    pyautogui.click(x=1800, y=900)
    pyautogui.click(x=1550, y=550, clicks=2, interval=0.1)

    # Upgrade Alchemist
    pyautogui.click(x=330, y=500, clicks=4, interval=0.1)
    pyautogui.click(x=330, y=650, clicks=2, interval=0.1)

def xp_farm(scroll_pos):
    # Click screen centre to close menus
    pyautogui.click(x=960, y=540)

    # Scroll to position
    pyautogui.moveTo(scroll_pos[0], scroll_pos[1])
    for i in range(0, 7):
        pyautogui.scroll(1)

    # Select and place Dart Monkey (Opens upgrade window)
    pyautogui.click(x=1800, y=200)
    pyautogui.click(x=125, y=575, clicks=2, interval=0.1)

    # Upgrade Sniper Monkey
    pyautogui.click(x=1550, y=500, clicks=4, interval=0.1)
    pyautogui.click(x=1550, y=650, clicks=4, interval=0.1)
    pyautogui.click(x=1550, y=800, clicks=4, interval=0.1)
