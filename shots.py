from Screenshoter import Screenshoter
import keyboard

def hetKeySF1(scr):
    print("SF1")
    scr.stop = True


scr = Screenshoter()
keyboard.add_hotkey('shift+F1', hetKeySF1, args=(scr, ), suppress=True, trigger_on_release=True)
scr.Start()