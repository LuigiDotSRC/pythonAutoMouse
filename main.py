import tkinter as tk
import ttkbootstrap as ttk

import pyautogui
import time
from datetime import datetime

def cornerClicks(numIterations, actiondelayseconds, screenWidth, screenHeight):
    time.sleep(2)
    intNumIterations = numIterations.get() 
    intActionDelaySeconds = actiondelayseconds.get() 
    output = ""

    for iter in range(intNumIterations):
        
        output = f"---------iteration: {iter+1}/{intNumIterations}\n"
        print(output)
   
        current_time = datetime.now().time()
        time_string = current_time.strftime('%H:%M:%S')
        text.insert(1.0,f"iteration: {iter+1} | time: {time_string}\n")

        mouseLocation = 10, 10 # top left 
        pyautogui.click(mouseLocation) 
        print(f"mouse location: {mouseLocation}")
        time.sleep(intActionDelaySeconds)

        mouseLocation = screenWidth - 10, 10 # top right 
        pyautogui.click(mouseLocation) 
        print(f"mouse location: {mouseLocation}")
        time.sleep(intActionDelaySeconds)

        mouseLocation = screenWidth - 10, screenHeight - 10 # bot right
        pyautogui.click(mouseLocation) 
        print(f"mouse location: {mouseLocation}")
        time.sleep(intActionDelaySeconds)

        mouseLocation = 10, screenHeight - 10 # bot left
        pyautogui.click(mouseLocation) 
        print(f"mouse location: {mouseLocation}")
        time.sleep(intActionDelaySeconds)

def AutoClick(numIterations, actiondelayseconds, screenWidth, screenHeight):   
    time.sleep(2)
    intNumIterations = numIterations.get() 
    intActionDelaySeconds = actiondelayseconds.get() 
    output = ""

    for iter in range(intNumIterations):
        
        output = f"---------iteration: {iter+1}/{intNumIterations}\n"
        print(output)
   
        current_time = datetime.now().time()
        time_string = current_time.strftime('%H:%M:%S')
        text.insert(1.0,f"iteration: {iter+1} | time: {time_string}\n")

        horizontalLocation = int(screenWidth/2)
        veritcalLocation = int(screenHeight/2)
 
        pyautogui.click(horizontalLocation,veritcalLocation,duration=0.01)
        pyautogui.click(horizontalLocation,veritcalLocation,duration=0.01)
        pyautogui.click(horizontalLocation,veritcalLocation,duration=0.01)
        pyautogui.click(horizontalLocation,veritcalLocation,duration=0.01)
        print(f"click: {iter+1}/{numIterations}")
        time.sleep(intActionDelaySeconds)
    
def SmallMove(numIterations, actiondelayseconds, screenWidth, screenHeight):
    intNumIterations = numIterations.get() 
    intActionDelaySeconds = actiondelayseconds.get() 
    output = ""

    for iter in range(intNumIterations):
        
        output = f"---------iteration: {iter+1}/{intNumIterations}\n"
        print(output)

        current_time = datetime.now().time()
        time_string = current_time.strftime('%H:%M:%S')
        text.insert(1.0,f"iteration: {iter+1} | time: {time_string}\n")

        pyautogui.move(5,0)
        pyautogui.move(-5,0)
        time.sleep(intActionDelaySeconds)    

# window 
window = ttk.Window(themename = "darkly")
window.title("Python Auto Mouse")
window.geometry("500x400")
window.resizable(False, False)

# variables
numIterations = tk.IntVar() 
actionDelaySeconds = tk.IntVar()
screenWidth, screenHeight = pyautogui.size()

# title 
title_label = ttk.Label(master = window, text = "Python Auto Mouse", font = "Calibri 24 bold")
title_label.pack()

# frame
frame = ttk.Frame(
    master = window
)
frame.pack()

frame2 = ttk.Frame(
    master = window
)
frame2.pack()

# buttons 
button1 = ttk.Button(
    master = frame,
    text = "Corner Clicks",
    state = "normal",
    width = "50",
    command = lambda: cornerClicks(numIterations, actionDelaySeconds, screenWidth, screenHeight)
)
button1.pack(pady = 5)

button2 = ttk.Button(
    master = frame,
    text = "Auto Click",
    state = "normal",
    width = "50",
    command = lambda: AutoClick(numIterations, actionDelaySeconds, screenWidth, screenHeight)
)
button2.pack(pady = 5)

button3 = ttk.Button(
    master = frame,
    text = "Small Move",
    state = "normal",
    width = "50",
    command = lambda: SmallMove(numIterations, actionDelaySeconds, screenWidth, screenHeight)
)
button3.pack(pady = 5)

#labels
label1 = ttk.Label(
    master = frame2, 
    text = "Number of iterations: ",
    font = "Calibri 12",
)
label1.grid(column = 1, row = 1)

label2 = ttk.Label(
    master = frame2, 
    text = "Action Delay (Seconds): ",
    font = "Calibri 12"
)
label2.grid(column = 1, row = 2)

# entry fields
entry1 = ttk.Entry(
    master = frame2,
    textvariable = numIterations,
)
entry1.grid(column = 2, row = 1)
entry1.insert(1,"5")

entry2 = ttk.Entry(
    master = frame2,
    textvariable = actionDelaySeconds,
)
entry2.grid(column = 2, row = 2)
entry2.insert(1,"1")

# output terminal 
text = tk.Text(
    master = window,
    width = "60",
    height = "10",
)
text.pack(pady = 5)

# run
window.mainloop()
