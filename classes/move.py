import pyautogui
import time
from ..automation.autoGUI import AutoGui


class Move():
    
    def __init__(self):
        self.auto_gui = AutoGui()




    def move_to_area(self, image_path, confidence=.95, count=0):
        """Move the mouse to the area of the screen where the image is located."""
        try:
            if count >= 20:
                print("Maximum number of attempts reached. Stopping...")
                return

            result = self.auto_gui.locate_on_screen(image_path, confidence=confidence)
            if result is not None:
                x, y, width, height = result
                c_x, c_y = self.auto_gui.move_center(x, y, width, height)
                print(f"Moving the mouse to the center of the area where the image {image_path} is located...")
                self.auto_gui.move_mouse(c_x, c_y)
                self.auto_gui.double_click(c_x, c_y)
                self.auto_gui.double_click(c_x, c_y)

                return c_x, c_y
            else:
                self.auto_gui.move_left()
                self.auto_gui.move_right()
                self.move_to_area(image_path, confidence=confidence, count=count+1)
            print(f"Image {image_path} not found on the screen.")
            
        except Exception as e:
            print(f"An error occurred while moving the mouse to the area of the screen: {e}")

    def move_to_npc(self, image_path, confidence=.70):
        """Move the mouse to the area of the screen where the image is located."""
        try:
            result = self.auto_gui.locate_on_screen(image_path, confidence=confidence)
            if result is not None:
                x, y, width, height = result
                c_x, c_y = self.auto_gui.move_center(x, y, width, height)
                print(f"Moving the mouse to [{c_x},{c_y}] where the image {image_path} is located...")
                self.auto_gui.move_mouse(c_x, c_y)
                self.auto_gui.double_click(c_x, c_y)
                self.auto_gui.press_key('enter')
                return c_x, c_y
            else:
                print(f"Image {image_path} not found on the screen.")
            
        except Exception as e:
            print(f"An error occurred while moving the mouse to the area of the screen: {e}")
    
