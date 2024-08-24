import time
import pyautogui, sys

def click(n, button="primary", interval=0.25):
    pyautogui.click(clicks=n, button=button, interval=interval)

def move(x, y, click=False):
    pyautogui.moveTo(x,y)
    
    if click == True:
        pyautogui.click()