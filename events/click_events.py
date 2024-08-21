import time
import pyautogui, sys
import random

def click(n):
    while n <= random.randint(20,200):
        pyautogui.moveTo(random.randint(0, 1920), random.randint(0, 1080))
        pyautogui.click(clicks=random.randint(2, 100))
        n+=1
        time.sleep(random.uniform(0, 2))