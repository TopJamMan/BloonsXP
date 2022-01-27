'''
from datetime import datetime
import time

start_time = datetime.now()
time.sleep(10)
end_time = start_time - datetime.now()


print(end_time.strftime('%m'))
'''

import pyautogui

print(pyautogui.pixelMatchesColor(950, 400, (255, 219, 0)))
