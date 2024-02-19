from ..classes import move
import os
import json

class SellBean():
        
    def __init__(self, race):
        self.move = move.Move()

        self.race = race
        
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

            print(f"Moving the mouse to the village area using image path: {location}")

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
                self.npc_keys = ["npc_moori1", "npc_moori2", "npc_moori3"]
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

            print(f"Moving the mouse to the village area using image path: {location}")

            move_result = self.move.move_to_area(image_path=location, confidence=.95)

            if not move_result:
                print("Error: Failed to move the mouse to the village area.")
                return

            print("Successfully moved the mouse to the village area.")

        except Exception as e:
            print(f"An error occurred while moving the mouse to the village area: {e}")

    def sell(self):
        self.move_to_village()
        self.click_npc()
        self.move_back_home()