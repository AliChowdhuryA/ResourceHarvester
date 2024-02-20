import time
import random
from ..automation.autoGUI import AutoGui
import json
import pyautogui

import os

class Harvester():
    def __init__(self, tree_level):
        self.auto_gui = AutoGui()
        self.tree_level = tree_level

        # Load the image paths from the JSON file
        image_paths = os.path.join(os.path.dirname(__file__), 'image_paths.json')
        with open(image_paths) as f:
            self.image_paths = json.load(f)
        
        coord_paths = 'D:\\1PythonWorks\\CSC1500\\FinalLab\\FinalLab\\BeanHarvester\\json_files\\hardCoords.json'
        with open(coord_paths) as f:
            self.coord_paths = json.load(f)

    def click_green_harvest_button(self):
        image_path = self.image_paths["green_harvest_button"]
        # Locate the "green harvest" button on the screen
        result = self.auto_gui.locate_on_screen(image_path, confidence=.70)
        if result is not None:
            x, y, width, height = result
            c_x, c_y = self.auto_gui.move_center(x, y, width, height)
            self.auto_gui.click(c_x, c_y)
            self.auto_gui.hard_click()
        else:
            print(f"Could not find the image {image_path} on the screen.")

    def click_bean_tree(self):
        # TODO: Make image path change based on what account is being used
        # We can do this when we call it in main

        image_path = self.image_paths[self.tree_level]
        print(image_path)
        # Locate the "bean tree" on the screen
        result = self.auto_gui.locate_on_screen(image_path, confidence=.70)
        if result is not None:
            x, y, width, height = result
            c_x, c_y = self.auto_gui.move_center(x, y, width, height)
            self.auto_gui.double_click(c_x, c_y)
            self.auto_gui.press_key('enter')
        else:
            print(f"Could not find the image {image_path} on the screen.")        
    def harvest(self):
        """calls all the functions in the correct order to harvest beans"""
        self.click_bean_tree()    
        self.click_green_harvest_button()
