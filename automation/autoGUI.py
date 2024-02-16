import time
import pyautogui

from pyautogui import hotkey

class AutoGui:
    def move_mouse(self, x, y):
        try:
            pyautogui.moveTo(x, y)
        except pyautogui.FailSafeException:
            print("FailSafeException: The mouse move operation was aborted.")
            # Handle the exception as needed
        except Exception as e:
            print(f"An error occurred while moving the mouse: {e}")
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
            print(f"An error occurred while locating the image: {e}")
    
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
                else:
                    pyautogui.write(char)
        except Exception as e:
            print(f"An error occurred while writing text: {e}")
            # Handle the exception as needed