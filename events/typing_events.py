import random
import pyautogui
import time

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','=']

def gibberish(count):
    gibberish_text = ""
    while count > 0:
        gibberish_text += characters[random.randint(0, len(characters) - 1)]
        count -= 1
        pyautogui.write(gibberish_text, interval=1)

