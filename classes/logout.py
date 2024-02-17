import time
import random
from ..automation.autoGUI import AutoGui
import json
import pyautogui

import os

class GameLogout():
    def __init__(self):
        self.auto_gui = AutoGui()

        # Load the image paths from the JSON file
        image_paths = os.path.join(os.path.dirname(__file__), 'image_paths.json')
        with open(image_paths) as f:
            self.image_paths = json.load(f)
        
        coord_paths = 'D:\\1PythonWorks\\CSC1500\\FinalLab\\FinalLab\\BeanHarvester\\json_files\\hardCoords.json'
        with open(coord_paths) as f:
            self.coord_paths = json.load(f)
    
    def find_and_click_change_account(self):
        """Presses up arrow one time and finds the change account button and clicks it."""
        self.auto_gui.press_key("up")
        image_paths = [self.image_paths["change_account_function_color1"], self.image_paths["change_account_function_color2"]]
        for image_path in image_paths:
            # Locate the "change account" button on the screen
            result = self.auto_gui.locate_on_screen(image_path, confidence=.90)
            if result is not None:
                x, y, width, height = result
                c_x, c_y = self.auto_gui.move_center(x, y, width, height)
                # self.auto_gui.click(c_x, c_y)
                self.auto_gui.hard_click()
                break

    def click_function_tab(self):
        image_paths = [self.image_paths["function_tab_color1"], self.image_paths["function_tab_color2"]]
        for image_path in image_paths:
            # Locate the "function" tab on the screen
            result = self.auto_gui.locate_on_screen(image_path, confidence=.70)
            if result is not None:
                x, y, width, height = result
                c_x, c_y = self.auto_gui.move_center(x, y, width, height)
                self.auto_gui.click(c_x, c_y)
                break  # If we found and clicked the tab, we can stop looking
        else:
            print(f"Could not find the images {image_paths} on the screen.")
    def click_logout(self):
        image_path = self.image_paths["logout_button"]
        # Locate the "logout" button on the screen
        result = self.auto_gui.locate_on_screen(image_path, confidence=.70)
        if result is not None:
            x, y, width, height = result
            c_x, c_y = self.auto_gui.move_center(x, y, width, height)
            self.auto_gui.click(c_x, c_y)
        else:
            print(f"Could not find the image {image_path} on the screen.")

    def click_menu(self):
        image_path = self.image_paths["menu_button"]
        # Locate the "menu" button on the screen
        result = self.auto_gui.locate_on_screen(image_path, confidence=.90)
        if result is not None:
            x, y, width, height = result
            c_x, c_y = self.auto_gui.move_center(x, y, width, height)
            self.auto_gui.click(c_x, c_y)
            
        else:
            print(f"Could not find the image {image_path} on the screen.")
        
    def logout(self):
        """calls all the functions in the correct order to logout"""
        self.click_menu()
        self.click_function_tab()
        self.find_and_click_change_account()
