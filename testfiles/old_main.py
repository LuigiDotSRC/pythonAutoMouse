import pyautogui
import time
from datetime import datetime

def cornerMouseClick(numIterations, actiondelayseconds, screenWidth, screenHeight):
    timestart = datetime.now().time()
    for iter in range(numIterations):
        print(f"---------iteration: {iter+1}/{intNumIterations}")

        mouseLocation = 10, 10 # top left 
        pyautogui.click(mouseLocation) 
        print(f"mouse location: {mouseLocation}")
        time.sleep(actiondelayseconds)

        mouseLocation = screenWidth - 10, 10 # top right 
        pyautogui.click(mouseLocation) 
        print(f"mouse location: {mouseLocation}")
        time.sleep(actiondelayseconds)

        mouseLocation = screenWidth - 10, screenHeight - 10 # bot right
        pyautogui.click(mouseLocation) 
        print(f"mouse location: {mouseLocation}")
        time.sleep(actiondelayseconds)

        mouseLocation = 10, screenHeight - 10 # bot left
        pyautogui.click(mouseLocation) 
        print(f"mouse location: {mouseLocation}")
        time.sleep(actiondelayseconds)

    timeend = datetime.now().time()
    print(f"--------- PROCESS FINISHED: {timeend}")
    print(f"TIME START: {timestart}")

def autoMouseClick(numIterations, actiondelayseconds, screenWidth, screenHeight):
    horizontalLocation = int(screenWidth/2)
    veritcalLocation = int(screenHeight/2)

    time.sleep(2) #safety delay -- can reach ~ 8 cps 
    for iter in range(numIterations):
        pyautogui.click(horizontalLocation,veritcalLocation,duration=0.01)
        pyautogui.click(horizontalLocation,veritcalLocation,duration=0.01)
        pyautogui.click(horizontalLocation,veritcalLocation,duration=0.01)
        pyautogui.click(horizontalLocation,veritcalLocation,duration=0.01)
        print(f"click: {iter+1}/{numIterations}")
        time.sleep(actiondelayseconds)

def smallMove(numIterations, actiondelayseconds, screenWidth, screenHeight):  
    timestart = datetime.now().time()
    for iter in range(numIterations):
        print(f"---------iteration: {iter+1}/{numIterations}")
        pyautogui.move(5,0)
        pyautogui.move(-5,0)
        time.sleep(actiondelayseconds)
    
    timeend = datetime.now().time()
    print(f"--------- PROCESS FINISHED: {timeend}")
    print(f"TIME START: {timestart}")

if __name__ == "__main__":
    # init variables 
    numIterations = 200
    actiondelayseconds = 2
    screenWidth, screenHeight = pyautogui.size()
    print(f"screen size: w{screenWidth}, h{screenHeight}")

    while(True):
        validOptions = ["1","2","3","q"]

        print('''
        OPTIONS:
        1 -- Corner Clicks 
        2 -- Auto Click
        3 -- Small Move
        q -- Quit
        ''')

        option = input("Enter an option  > ")
        
        if(option not in validOptions):
            print("Enter a valid option")
        elif(option == "q"):
            break

        else:
            if(option == "1"):
                cornerMouseClick(numIterations,actiondelayseconds,screenWidth,screenHeight)
            elif(option == "2"):
                autoMouseClick(numIterations,actiondelayseconds,screenWidth,screenHeight)
            elif(option == "3"):
                smallMove(numIterations,actiondelayseconds,screenWidth,screenHeight)
    
    print("quit")