import pyautogui

def type_text(text, with_enter=False):
    pyautogui.write(text, interval=1)
    if with_enter == True:
        pyautogui.press('enter')

