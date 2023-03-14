#Bean harvest functions
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from exception_handler import handle_exception

MAX_ATTEMPTS = 5
ATTEMPT_DELAY = 2
TIMEOUT = 10
#play acc

def playAcc():
    
    time.sleep(.5)
    click(850,490)
    time.sleep(0.05)

def locateImage(image_path, confid):
    coords = None
    attempts = 0
    start_time = time.time()
    while coords is None and attempts < MAX_ATTEMPTS and time.time() - start_time < TIMEOUT:
        attempts +=1
        coords = pyautogui.locateOnScreen(image_path, confidence=confid)
        if coords is not None:
            print(coords)
            return coords
        else:
            print("Attempt failed, will try again. No.: ", attempts)
            time.sleep(ATTEMPT_DELAY)
    print("Could not find image on screen.")
    return None
def long_click(c_coords):
    pyautogui.moveTo(c_coords, duration=0.1)
    time.sleep(.05)
    # Press and hold the left mouse button
    pyautogui.mouseDown(button='left')

    # Wait for 2 seconds
    time.sleep(2)

    # Release the left mouse button
    pyautogui.mouseUp(button='left')
def selectTree():
    try:
        coords = locateImage('DBOPics\Lv7BeanTreeWHarvest.png',.8)
        if coords is None:
            raise ValueError("Tree not found")
        center = pyautogui.center(coords)
        center = (center[0], center[1] - 150)  # modify y-value to go up by 50 pixels
        pyautogui.moveTo(center, duration=0.1)
        time.sleep(.05)
        pyautogui.click()
    except Exception as e:
        handle_exception(e)


def harvestClick(): #harvestClick
    try:
        coords = locateImage('DBOPics\Harvest_Button.JPG',.8)
        if coords is None:
            raise ValueError("Harvest button not found")
            # Check if the image is still on the screen
        if pyautogui.locateOnScreen('DBOPics\Harvest_Button.JPG', confidence=0.65) is not None:
            pyautogui.press('enter')
        else:
            print("Could not find Harvest Button on screen.")
    except Exception as e:
        handle_exception(e)

def moveToMoori():
    try:
        coords = locateImage('DBOPics/full_beans.png',.8)
        print("Move left!")
        pyautogui.keyDown('left')  # hold down the left key
        time.sleep(1)
        pyautogui.keyUp('left')
        print("done")
        coords = locateImage('DBOPics/moori_header.png',.8)
        if coords is None:
            raise ValueError("Moori Village Prompt not found")
        center = pyautogui.center(coords)
        pyautogui.moveTo(center, duration=0.1)
        time.sleep(.05)
        pyautogui.click()
    except Exception as e:
        handle_exception(e)

def click_dende():
    try:
        coords = locateImage('DBOPics/village_dende.png',.8)
        if coords is None:
            raise ValueError("Dende not found(Change zones)")
        center = pyautogui.center(coords)
        pyautogui.moveTo(center, duration=0.1)
        time.sleep(.05)
        pyautogui.doubleClick()
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(2)
    except Exception as e:
        handle_exception(e)

def click_shop():
    try:
        coords = locateImage('DBOPics/dende_shop.png',.8)
        if coords is None:
            raise ValueError("Shop icon not found, Candy?")
        center = pyautogui.center(coords)
        pyautogui.moveTo(center, duration=0.1)
        time.sleep(1)
        
        if pyautogui.locateOnScreen('DBOPics\dende_shop.png', confidence=0.65) is not None:
            pyautogui.press('enter')
            for i in range(3):
                time.sleep(1)
                pyautogui.press('right')
        else:
            print("Could not find dendes shop on screen.")
    except Exception as e:
        handle_exception(e)   

def locate_beans():
    #press down until beans are shown
    start_time = time.time()
    timeout = 60  # timeout after 60 seconds
    count = 0
    while time.time() - start_time < timeout:
        count += 1
        if pyautogui.locateOnScreen('DBOPics\level_7_beans_stack.png', confidence=0.85) is not None:
            pyautogui.press('enter')
            break
            #return True  # beans found, exit function
        else:
            if count <=20:
                pyautogui.press('down')
            else:
                #reset count
                coords = locateImage('DBOPics/2.png',.8)
                center = pyautogui.center(coords)
                long_click(center)
                count = 0
def sell_beans():
    try:
        coords = locateImage('DBOPics/sale_button.png',.8)
        if coords is None:
            raise ValueError("Sale icon not found, Shop not open?")
        center = pyautogui.center(coords)
        pyautogui.moveTo(center, duration=0.1)
        time.sleep(.05)
        # Press and hold the left mouse button
        pyautogui.mouseDown(button='left')

        # Wait for 2 seconds
        time.sleep(2)

        # Release the left mouse button
        pyautogui.mouseUp(button='left')
    except Exception as e:
        handle_exception(e)
def confirm():
    try:
        coords = locateImage('DBOPics/yes.png',.8)
        if coords is None:
            raise ValueError("Yes button not found")
        center = pyautogui.center(coords)
        long_click(center)
    except Exception as e:
        handle_exception(e)
def go_back_home():
    try:
        coords = locateImage('DBOPics/redX.png',.8)
        if coords is None:
            raise ValueError("Red X not found")
        center = pyautogui.center(coords)
        pyautogui.moveTo(center, duration=0.1)
        time.sleep(.05)
        # Press and hold the left mouse button
        pyautogui.mouseDown(button='left')
        # Wait for 2 seconds
        time.sleep(2)
        # Release the left mouse button
        pyautogui.mouseUp(button='left')
        print("Move right!")
        time.sleep(2)
        pyautogui.keyDown('right')  # hold down the right key
        time.sleep(.5)
        pyautogui.keyUp('right')
        print("done")
        coords = locateImage('DBOPics/moori_house.png',.8)
        if coords is None:
            raise ValueError("Moori Village Prompt not found")
        center = pyautogui.center(coords)
        pyautogui.moveTo(center, duration=0.1)
        time.sleep(.05)
        pyautogui.click()
        move('right',.5)
    except Exception as e:
        handle_exception(e)
def click_buyback():
    try:
        coords = locateImage('DBOPics/dende_buyback.png',.8)
        if coords is None:
            raise ValueError("Buyback icon not found, Candy?")
        center = pyautogui.center(coords)
        long_click(center)
    except Exception as e:
        handle_exception(e)
def re_harvest():
    try:
        coords = locateImage('DBOPics/can_harvest_17.png',.8)
        if coords is None:
            raise ValueError("Can Harvest not found")
        center = pyautogui.center(coords)
        long_click(center)
    except Exception as e:
        handle_exception(e)
def buy_with_110_gold():
    try:
        coords = locateImage('DBOPics/buy_with_110.png',.8)
        if coords is None:
            raise ValueError("buy_with_110.png not found")
        center = pyautogui.center(coords)
        long_click(center)
    except Exception as e:
        handle_exception(e)
def buyback_beans():
    start_time = time.time()
    timeout = 20  # timeout after 60 seconds
    count = 0
    while time.time() - start_time < timeout:
        try:
            coords = locateImage('DBOPics/senzu_beans.png',.8)
            if coords is None:
                raise ValueError("Can Harvest not found")
            center = pyautogui.center(coords)
            long_click(center)
            time.sleep(1)
            buy_with_110_gold()
        except Exception as e:
            handle_exception(e)

def move(direction, seconds):
    time.sleep(2)
    pyautogui.keyDown(direction)  # hold down the left key
    time.sleep(seconds)
    pyautogui.keyUp(direction)
def click_menu():
    try:
        coords = locateImage('DBOPics/orange_carrot.png',.8)
        if coords is None:
            raise ValueError("orange_carrot.png not found")
        center = pyautogui.center(coords)
        long_click(center)
    except Exception as e:
        handle_exception(e)
def click_function():
#remake when youre better
        pyautogui.press('left')

def change_acc_button():
    try:
        time.sleep(.5)
        pyautogui.press('up')
        coords = locateImage('DBOPics/change_acc.png',.8)
        if coords is None:
            raise ValueError("change_acc.png not found")
        center = pyautogui.center(coords)
        long_click(center)
    except Exception as e:
        handle_exception(e)   

def click_green_x():
    try:
        time.sleep(.5)
        long_click(x=1087, y=555)
    except Exception as e:
        handle_exception(e)

def enter_acc():
    
