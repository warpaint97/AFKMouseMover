# AFKMouseMover
This python program will move your mouse automatically when you are AFK during a game to avoid being kicked.\
You can customize the config variables within the AFKMouseMover.py script.
```
# config
timeLimit = 10 # time limit in seconds until AFK Mode kicks in
updateTime = 1 # time between mouse movements during AFK mode
speed = 0.5 # time in seconds to reach next mouse position
screenFraction = 0.3 # move the mouse within the screen fraction from the center. screenFraction must be <= 1 and > 0.
```
 
### Dependencies
- pyautogui

Use `pip install pyautogui` to install the package.
