import sys
import os
import pyscreenshot as ImageGrab
import pythoncom, pyHook
import time
import threading

from __builtin__ import raw_input

dirpath = ""

def printScreen():
    dest_dir = dirpath + '\\'
    now = str(int(time.time()))
    im = ImageGrab.grab()
    ImageGrab.grab_to_file(dest_dir + now + '.png')


def right_down(event):
    t = threading.Thread(target=printScreen) #added to queue
    t.start()
    return True


if __name__ == "__main__":

    if len(sys.argv) < 2:
        dirpath = raw_input("Paste the destination folder path \n")
    else:
        dirpath = sys.argv[1]

    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


    hm = pyHook.HookManager()
    hm.SubscribeMouseRightDown(right_down)
    hm.HookMouse()
    pythoncom.PumpMessages()
    hm.UnhookMouse()
