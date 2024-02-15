import time
import random
from ..automation.autoGUI import AutoGui
import json
import pyautogui

import os

class GameLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.auto_gui = AutoGui()

        # Load the image paths from the JSON file
        file_path = os.path.join(os.path.dirname(__file__), 'image_paths.json')
        with open(file_path) as f:
            self.image_paths = json.load(f)
    def simulate_mouse_movement(self):
        image_path = self.image_paths["change_account"]
        # Locate the "change account" button on the screen
        result = self.auto_gui.locate_on_screen(image_path)
        if result is not None:
            x, y, width, height = result
            c_x, c_y = self.auto_gui.move_center(x, y, width, height)
            self.auto_gui.click(c_x, c_y)
            
        else:
            print(f"Could not find the image {image_path} on the screen.")
    def simulate_key_presses(self):
        # Simulate key presses code here
        pass

    def login(self):
        # Simulate mouse movement and key presses to login
        self.simulate_mouse_movement()
        self.simulate_key_presses()

        # Wait for login process to complete
        time.sleep(random.uniform(1, 3))

        # Check if login was successful
        if self.is_logged_in():
            print("Login successful!")
        else:
            print("Login failed!")

    def is_logged_in(self):
        # Check if user is logged in
        # Return True or False based on the login status
        pass
