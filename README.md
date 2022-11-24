# AFKMouseMover
This python program will move your mouse automatically when you are AFK during a game to avoid being kicked.

### Run
To run the AFK Mouse Mover, simply type `python AFKMouseMover.py` in command prompt or double click the `run.bat` batch file.
If the pyautogui package is not installed you will have to run `pip install pyautogui` in the command prompt first.

### Control
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
