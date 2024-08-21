import time
import sys
import random
import webbrowser

firefox_path = '/usr/bin/firefox'
chromium_path = '/snap/bin/chromium'

firefox = webbrowser.get(firefox_path)

def open(n):
    while n <= random.randint(5,10):
        firefox.open_new_tab('https://google.com/')
        n+=1
        time.sleep(random.uniform(5, 10))