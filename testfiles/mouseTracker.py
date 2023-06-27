import pyautogui as p
import time as t 

delaySeconds = 1
iterations = 20

for i in range(iterations):
    print(p.position())
    t.sleep(delaySeconds)