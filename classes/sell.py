import time
from ..classes import move
import os
import json
from ..automation.autoGUI import AutoGui

import logging
logger = logging.getLogger('my_logger')

class SellBean():
        
    def __init__(self, race):
        self.move = move.Move()

        self.race = race

        self.auto_gui = AutoGui()
        
        image_paths = os.path.join(os.path.dirname(__file__), 'image_paths.json')
        with open(image_paths) as f:
            self.image_paths = json.load(f)
        
        coord_paths = 'D:\\1PythonWorks\\CSC1500\\FinalLab\\FinalLab\\BeanHarvester\\json_files\\hardCoords.json'
        with open(coord_paths) as f:
            self.coord_paths = json.load(f)

        location_paths = 'D:\\1PythonWorks\\CSC1500\\FinalLab\\FinalLab\\BeanHarvester\\json_files\\locations.json'
        with open(location_paths) as f:
            self.location_paths = json.load(f)

        account_emails = 'D:\\1PythonWorks\\CSC1500\\FinalLab\\FinalLab\\BeanHarvester\\json_files\\account_files.json'
        with open(account_emails) as f:
            self.account_emails = json.load(f)

        npc_paths = 'D:\\1PythonWorks\\CSC1500\\FinalLab\\FinalLab\\BeanHarvester\\json_files\\npcs.json'
        with open(npc_paths) as f:
            self.npc_paths = json.load(f)

    def yes_button(self):
        """Click the yes button."""
        try:
            image_path = self.image_paths["yes_button"]
            # Locate the "green harvest" button on the screen
            result = self.auto_gui.locate_on_screen(image_path, confidence=.70)
            if result is not None:
                x, y, width, height = result
                c_x, c_y = self.auto_gui.move_center(x, y, width, height)
                self.auto_gui.click(c_x, c_y)
                self.auto_gui.hard_click()
            else:
                print(f"Could not find the image {image_path} on the screen.")

        except Exception as e:
            print(f"An error occurred while clicking the yes button: {e}")

    def x_button(self):
        """Click the x button."""
        try:
            image_path = self.image_paths["x_button"]
            # Locate the "green harvest" button on the screen
            result = self.auto_gui.locate_on_screen(image_path, confidence=.70)
            if result is not None:
                x, y, width, height = result
                c_x, c_y = self.auto_gui.move_center(x, y, width, height)
                self.auto_gui.click(c_x, c_y)
                self.auto_gui.hard_click()
            else:
                print(f"Could not find the image {image_path} on the screen.")

        except Exception as e:
            print(f"An error occurred while clicking the x button: {e}")

    def sell_button(self):
        """Click the sell button."""
        try:
            image_path = self.image_paths["sell_button"]
            # Locate the "green harvest" button on the screen
            result = self.auto_gui.locate_on_screen(image_path, confidence=.70)
            if result is not None:
                x, y, width, height = result
                c_x, c_y = self.auto_gui.move_center(x, y, width, height)
                self.auto_gui.click(c_x, c_y)
                self.auto_gui.hard_click()
            else:
                print(f"Could not find the image {image_path} on the screen.")

        except Exception as e:
            print(f"An error occurred while clicking the sell button: {e}")

    def locate_bean(self):
        """Uses drag_menu to locate the bean in the inventory, if it doesn't find it at first, it will scroll again to find it."""
        try:
            print("Looking for the bean in the inventory...")
            location = self.image_paths["senzu_bean"]
            if not location:
                print("Error: Bean not found.")
                return
            for i in range(5):
                print(f"Dragging the inventory until bean is found")
                self.drag_menu()
                result = self.auto_gui.locate_on_screen(location, confidence=.95)
                if result is not None:
                    print("Bean found in inventory")
                    x, y, width, height = result
                    c_x, c_y = self.auto_gui.move_center(x, y, width, height)
                    self.auto_gui.move_mouse(c_x, c_y)
                    self.auto_gui.hard_click()
                    time.sleep(1)
                    self.sell_button()
                    time.sleep(1)
                    self.yes_button()
                    break
                print("Bean not found in inventory, scrolling again")
                logger.info(f"count: {i}")




        except Exception as e:
            print(f"An error occurred while dragging the menu bar: {e}")

    def drag_menu(self):
        """Drag the menu to the top of the screen."""
        try:
            print("Looking for the menu bar...")
            location = self.image_paths["equipment_bar"]
            if not location:
                print("Error: Menu bar not found.")
                return
            print(f"Dragging the menu bar to the top of the screen using image path: {location}...")
            self.auto_gui.drag_to_top(image_path=location, confidence=.95, x_offset=0, y_offset=300)
            print("Successfully dragged the menu bar to the top of the screen.")

        except Exception as e:
            print(f"An error occurred while dragging the menu bar: {e}")

    def shop_button(self):
        """Click the shop button."""
        try:
            print("Looking for the shop button...")
            location = self.image_paths["shop_button"]
            if not location:
                print("Error: Shop Button not found.")
                return
            print(f"Clicking the shop button using image path: {location}...")
            self.auto_gui.click_button(image_path=location, confidence=.95)
            print("Successfully clicked the shop button.")

        except Exception as e:
            print(f"An error occurred while clicking the shop button: {e}")


    def move_back_home(self):
        """move player back to village"""
        try:
            if self.race == "earth":
                location = self.location_paths["aru_village_gohan_house"]
            elif self.race == "namek":
                location = self.location_paths["moori_village_moori_house"]
            else:
                location = self.location_paths["kakalot_village_broly_house"]

            if not location:
                print("Error: Image path not found.")
                return
            # if x button is present, click it
            self.x_button()
            time.sleep(1)

            print(f"Moving the mouse to the village area using image path: {location}")

            if self.race != "earth":
                self.auto_gui.move_right()

            move_result = self.move.move_to_area(image_path=location, confidence=.70)


            if not move_result:
                print("Error: Failed to move the mouse to the village area.")
                return

            print("Successfully moved the mouse to the village area.")

        except Exception as e:
            print(f"An error occurred while moving the mouse to the village area: {e}")


    def click_npc(self):
        """Click the NPC to sell the beans."""
        try:
            if self.race == "earth":
                self.npc_keys = ["npc_bulma1", "npc_bulma2", "npc_bulma3"]
            elif self.race == "namek":
                self.npc_keys = ["npc_dende1", "npc_dende2", "npc_dende3"]
            else:
                self.npc_keys = ["npc_appule1", "npc_appule2", "npc_appule3"]
            
            for key in self.npc_keys:
                location = self.npc_paths[key]
                if not location:
                    print(f"Error: Image path for {key} not found.")
                    continue

                print(f"Looking for {key} using image path: {location}")
                move_result = self.move.move_to_npc(image_path=location, confidence=.70)
                if not move_result:
                    self.move.move_to_npc(image_path=location, confidence=.70)
                    print(f"Error: Failed to click the {key}.")

                if self.race == "saiyan":
                    self.auto_gui.press_key('enter')


                if not move_result:
                    print(f"Error: Failed to click the {key}.")
                    continue

                print(f"Successfully clicked the {key}.")
                break

        except Exception as e:
            print(f"An error occurred while clicking the NPC: {e}")

    def move_to_village(self):
        """Move the mouse to the village area."""

        if self.race == "earth":
            location = self.location_paths["gohan_house_aru_village"]
        elif self.race == "namek":
            location = self.location_paths["moori_house_moori_village"]
        else:
            location = self.location_paths["broly_house_kakalot_village"]

        try:
            # location = self.location_paths["moori_house_moori_village"]

            if not location:
                print("Error: Image path not found.")
                return
            
            if self.race == "namek":
                self.auto_gui.move_left()

            print(f"Moving the mouse to the village area using image path: {location}")

            move_result = self.move.move_to_area(image_path=location, confidence=.95)

            if not move_result:
                logger.info("Error: Failed to move the mouse to the village area.")
                return

            logger.info("Successfully moved the mouse to the village area.")

        except Exception as e:
            logger.info(f"An error occurred while moving the mouse to the village area: {e}")

    def sell(self):
        self.move_to_village()
        self.click_npc()
        self.shop_button()
        self.locate_bean()

        self.move_back_home()
        