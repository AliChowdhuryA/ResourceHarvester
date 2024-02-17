import time
import random
from ..automation.autoGUI import AutoGui
import json
import pyautogui

import os

class GameLogin():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.auto_gui = AutoGui()

        # Load the image paths from the JSON file
        image_paths = os.path.join(os.path.dirname(__file__), 'image_paths.json')
        with open(image_paths) as f:
            self.image_paths = json.load(f)
        
        coord_paths = 'D:\\1PythonWorks\\CSC1500\\FinalLab\\FinalLab\\BeanHarvester\\json_files\\hardCoords.json'
        with open(coord_paths) as f:
            self.coord_paths = json.load(f)

        account_emails = 'D:\\1PythonWorks\\CSC1500\\FinalLab\\FinalLab\\BeanHarvester\\json_files\\account_files.json'
        with open(account_emails) as f:
            self.account_emails = json.load(f)

    def click_login(self):
        image_path = self.image_paths["login_button"]
        # Locate the "login" button on the screen
        result = self.auto_gui.locate_on_screen(image_path, confidence=.70)
        if result is not None:
            x, y, width, height = result
            c_x, c_y = self.auto_gui.move_center(x, y, width, height)
            self.auto_gui.click(c_x, c_y)
        else:
            print(f"Could not find the image {image_path} on the screen.")

    def click_ok(self):
        image_path = self.image_paths["login_ok_button"]
        # Locate the "ok" button on the screen
        result = self.auto_gui.locate_on_screen(image_path, confidence=.70)
        if result is not None:
            x, y, width, height = result
            c_x, c_y = self.auto_gui.move_center(x, y, width, height)
            self.auto_gui.click(c_x, c_y)
            time.sleep(1)
        else:
            print(f"Could not find the image {image_path} on the screen.")
      
    def enter_username(self):
        """Clears the username field and enters the username."""
        clear_username_field = self.coord_paths["clear_username_field"]
        x,y = clear_username_field

        # self.auto_gui.move_mouse(x, y)
        self.auto_gui.click(x, y)

        # for account in self.account_emails["accounts"]:
        # # Click on the username field
        #     email = account["email"]
        #     break
        time.sleep(1)
        self.auto_gui.write(self.username)

    def click_change_account(self):
        image_path = self.image_paths["change_account"]
        # Locate the "change account" button on the screen
        result = self.auto_gui.locate_on_screen(image_path, confidence=.95)
        if result is not None:
            x, y, width, height = result
            c_x, c_y = self.auto_gui.move_center(x, y, width, height)
            self.auto_gui.click(c_x, c_y)
        else:
            print(f"Could not find the image {image_path} on the screen.")

    def simulate_key_presses(self):
        # Simulate key presses code here
        pass
    def simulate_mouse_movement(self):
        # Simulate mouse movement code here
        pass

    def login(self):
        # Simulate mouse movement and key presses to login
        self.click_change_account()
        self.enter_username()
        self.click_ok()
        self.click_login()

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
