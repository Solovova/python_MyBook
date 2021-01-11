import pyscreenshot
import pyautogui
import time

#80 1000
#50 650 1270 1880
def do_shots(first: int):
    im = pyscreenshot.grab(bbox=(50,80,650,1000))
    im.save("pages\\"+ str(first) + ".png")
    im = pyscreenshot.grab(bbox=(650,80,1270,1000))
    im.save("pages\\"+ str(first+1) + ".png") 
    im = pyscreenshot.grab(bbox=(1270,80,1880,1000))
    im.save("pages\\"+ str(first+2) + ".png")   

page = 1
for i in range(600):
    do_shots(page)
    page += 3
    pyautogui.moveTo(1880,1000)
    pyautogui.click()
    time.sleep(0.5)
    if (pyautogui.position().x != 1880):
        break