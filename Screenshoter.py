import pyscreenshot
import pyautogui
import time

class Screenshoter:
  stop = True

  def numToStr(self,i:int):
    s = str(i)
    while (len(s) != 4):
        s = "0" + s
    return s

  def do_shots(self, first: int):
    im = pyscreenshot.grab(bbox=(50,80,650,1000))
    im.save("pages\\"+ self.numToStr(first) + ".png")
    im = pyscreenshot.grab(bbox=(650,80,1270,1000))
    im.save("pages\\"+ self.numToStr(first+1) + ".png") 
    im = pyscreenshot.grab(bbox=(1270,80,1880,1000))
    im.save("pages\\"+ self.numToStr(first+2) + ".png")

  def Start(self):
    self.stop = False
    page = 1
    for i in range(1000):
      self.do_shots(page)
      page += 3
      print(page)
      pyautogui.moveTo(1880,1000)
      pyautogui.click()
      time.sleep(0.5)
      if (self.stop):
          break
