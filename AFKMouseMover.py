# author: Aaron Justin Bishop
# date: 11-24-2022
# decription: This python code will keep moving your mouse when you are AFK in a game.

import pydirectinput as pdi
import random
import time
import keyboard
import threading

######################################################################################################################
# config
timeLimit = 10 # time limit in seconds until AFK Mode kicks in
updateTime = 2 # time between mouse movements during AFK mode
duration = 1.5 # time in seconds to reach next mouse position
screenFraction = 0.2 # move the mouse within the screen fraction from the center. screenFraction must be <= 1 and > 0.
######################################################################################################################

# interpolate values
def lerp(origin, target, value):
    return origin + (target - origin) * value


# threading function for key listener
def keyListener(val):
    while True:
        val[0] = keyboard.read_key()

# function for mouse movement
def moveCursor(origin, target, t):
    global keyValue
    timer = 0.0
    while timer < t:
        start_time = time.time()
        value = timer/t
        x = int(lerp(origin[0], target[0], value))
        y = int(lerp(origin[1], target[1], value))
        pdi.moveTo(x, y)
        if pdi.position() != (x,y) or keyValue[0] != None:
            break
        elapsed = time.time() - start_time
        timer += elapsed



# program
if __name__ == '__main__':
    # internal variables
    last_pos = None
    counter = 0
    afkMode = False
    isMoving = False
    scale = screenFraction/2 + 0.5

    # threading for key listener
    keyValue = [None]
    listener = threading.Thread(target=keyListener, args=(keyValue,), daemon=True)
    listener.start()

    #main program loop
    print('Running AFK Mouse Mover.')
    while True:
        if counter > 0 <= timeLimit and not afkMode:
            print(f'{timeLimit - counter} seconds before AFK is detected.')

        if counter >= timeLimit:
            if not afkMode:
                print('AFK has been detected. Mouse is being moved.')
            afkMode = True
            x = random.randint((1-scale)*pdi.size()[0], scale*pdi.size()[0])
            y = random.randint((1-scale)*pdi.size()[1], scale*pdi.size()[1])

            moveCursor(pdi.position(), (x,y), duration)
            last_pos = pdi.position()

        time.sleep(1) if not afkMode else time.sleep(updateTime)
        if last_pos == pdi.position() and keyValue[0] == None:
            if not afkMode:
                counter += 1
        else:
            if counter > 0:
                print('Activity has been detected. AFK timer has been reset. Press [Ctrl+C] to quit.')
            counter = 0
            afkMode = False
            keyValue[0] = None
        last_pos = pdi.position()