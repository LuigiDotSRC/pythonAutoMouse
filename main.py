import pyautogui
import time

def cornerMouseClick(numIterations, actiondelayseconds, screenWidth, screenHeight):
    for iter in range(numIterations):
        print(f"---------iteration: {iter+1}/{numIterations}")

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

def autoMouseClick(numIterations, actiondelayseconds, screenWidth, screenHeight):
    horizontalLocation = int(screenWidth/2)
    veritcalLocation = int(screenHeight/2)

    time.sleep(2) #safety delay
    for iter in range(numIterations):
        pyautogui.click(horizontalLocation,veritcalLocation)
        print(f"click: {iter+1}/{numIterations}")
        time.sleep(actiondelayseconds)
        
if __name__ == "__main__":
    # init variables 
    numIterations = 4
    actiondelayseconds = 2
    screenWidth, screenHeight = pyautogui.size()
    print(f"screen size: w{screenWidth}, h{screenHeight}")

    while(True):
        validOptions = ["1","2","3","q"]

        print('''
        OPTIONS:
        1 -- Corner Clicks 
        2 -- Auto Click
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
    
    print("quit")