# author: Aaron Justin Bishop
# date: 11-24-2022
# decription: This python code will keep moving your mouse when you are AFK in a game.

import pyautogui as pag
import random
import time
import keyboard
import threading

######################################################################################################################
# config
timeLimit = 10 # time limit in seconds until AFK Mode kicks in
updateTime = 1 # time between mouse movements during AFK mode
speed = 0.5 # time in seconds to reach next mouse position
screenFraction = 0.3 # move the mouse within the screen fraction from the center. screenFraction must be <= 1 and > 0.
######################################################################################################################

# threading function
def keyListener(val):
    while True:
        val[0] = keyboard.read_key()

# program
if __name__ == '__main__':
    # internal variables
    last_pos = None
    counter = 0
    afkMode = False
    scale = screenFraction/2 + 0.5

    # threading for key listener
    keyValue = [None]
    thread = threading.Thread(target=keyListener, args=(keyValue,), daemon=True)
    thread.start()

    #main program loop
    print('Running AFK Mouse Mover.')
    while True:
        if counter > 0 <= timeLimit and not afkMode:
            print(f'{timeLimit - counter} seconds before AFK is detected.')

        if counter >= timeLimit:
            if not afkMode:
                print('AFK has been detected. Mouse is being moved.')
            afkMode = True
            x = random.randint((1-scale)*pag.size().width, scale*pag.size().width)
            y = random.randint((1-scale)*pag.size().height, scale*pag.size().height)

            pag.moveTo(x, y, speed)
            last_pos = pag.position()

        time.sleep(1) if not afkMode else time.sleep(updateTime)
        if last_pos == pag.position() and keyValue[0] == None:
            if not afkMode:
                counter += 1
        else:
            if counter > 0:
                print('Activity has been detected. AFK timer has been reset. Press [Ctrl+C] to quit.')
            counter = 0
            afkMode = False
            keyValue[0] = None
        last_pos = pag.position()