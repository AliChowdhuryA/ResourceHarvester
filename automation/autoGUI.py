import random
import time
import pyautogui

from pyautogui import hotkey

import os
import json

class AutoGui:

    def drag_to_top(self, image_path, confidence=.95, x_offset=0, y_offset=0):
        try:
            result = self.locate_on_screen(image_path, confidence=confidence)
            if result is not None:
                x, y, width, height = result
                x -= x_offset
                y += y_offset
                c_x, c_y = self.move_center(x, y, width, height)
                c_x += x_offset
                c_y -= y_offset
                print(f"Dragging the menu bar to the top of the screen using image path: {image_path}...")
                pyautogui.dragTo(c_x, c_y, duration=.3, tween=pyautogui.easeInOutQuad)
                return c_x, c_y
            print(f"Image {image_path} not found on the screen.")
        except Exception as e:
            print(f"An error occurred while dragging the menu bar: {e}")
            # Handle the exception as needed

    def click_button(self, image_path, confidence=.95):
        try:
            time.sleep(2)
            result = self.locate_on_screen(image_path, confidence=confidence)
            if result is not None:
                x, y, width, height = result
                c_x, c_y = self.move_center(x, y, width, height)
                print(f"Clicking the button using image path: {image_path}...")
                self.click(c_x, c_y)
                self.hard_click()
                return c_x, c_y
            print(f"Image {image_path} not found on the screen.")
        except Exception as e:
            print(f"An error occurred while clicking the button: {e}")
            # Handle the exception as needed


    def move_right(self):
        try:
            delay = random.uniform(0.05, 0.20)


            pyautogui.keyDown("right")
            time.sleep(delay)
            pyautogui.keyUp("right")
        except Exception as e:
            print(f"An error occurred while moving right: {e}")
            # Handle the exception as needed

    def move_left(self):
        try:
            delay = random.uniform(0.05, 0.20)
            pyautogui.keyDown("left")
            time.sleep(delay)
            pyautogui.keyUp("left")
        except Exception as e:
            print(f"An error occurred while moving left: {e}")
            # Handle the exception as needed

    def check_loading(self, image_path, confidence=.95):
        """Check if the game is still loading."""
        print(image_path)

        try:
            time.sleep(3)
            result = self.locate_on_screen(image_path, confidence=confidence)
            if result is not None:
                print("Game is still loading. Wait for 5 seconds...")
                time.sleep(5)
                return True
            print("Game is done loading.")
            return False
        except Exception as e:
            print(f"An error occurred while checking if the game is loading: {e}")
            # Handle the exception as needed

    def move_mouse(self, x, y):
        try:
            pyautogui.moveTo(x, y)
        except pyautogui.FailSafeException:
            print("FailSafeException: The mouse move operation was aborted.")
            # Handle the exception as needed
        except Exception as e:
            print(f"An error occurred while moving the mouse: {e}")
            # Handle the exception as needed

    def press_key(self, key):
        try:
            pyautogui.press(key)
        except Exception as e:
            print(f"An error occurred while pressing the key: {e}")
            # Handle the exception as needed
    def press_keys(self, keys):
        try:
            pyautogui.typewrite(keys)
        except Exception as e:
            print(f"An error occurred while typing keys: {e}")
            # Handle the exception as needed
    
    def locate_on_screen(self, image_path, confidence=.95):
        try:
            time.sleep(1)
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            
            if location is None:
                raise Exception(f"Image {image_path} not found on screen.")
            return location
        except Exception as e:
            print(f"An error occurred while locating {image_path} image: {e}")
    
    def hard_click(self):
        """Simulates a click and no movement of the mouse. This is useful for clicking on stubborn buttons."""
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()
    
    def double_click(self, x, y, button="left"):
        try:
            pyautogui.doubleClick(x, y, button=button)
        except Exception as e:
            print(f"An error occurred while double clicking the mouse: {e}")
            # Handle the exception as needed

    def click(self, x, y, button="left"):
        try:
            pyautogui.click(x, y, button=button)
        except Exception as e:
            print(f"An error occurred while clicking the mouse: {e}")
            # Handle the exception as needed

    def move_center(self, x, y, width, height):
        center_x = x + width / 2
        center_y = y + height / 2
        self.move_mouse(center_x, center_y)
        return center_x, center_y
    
    def write(self, text):
        try:
            for char in text:
                if char == "@":
                    pyautogui.keyDown("shift")
                    pyautogui.keyDown("2")
                    pyautogui.keyUp("2")
                    pyautogui.keyUp("shift")
                else:
                    pyautogui.write(char)
        except Exception as e:
            print(f"An error occurred while writing text: {e}")
            # Handle the exception as needed
    
