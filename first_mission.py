import characters
import random

choose_zone = input("Choose your zone: ")
zones = ["Forest", "Dungeon", "Jungle", "Desert"]
quest_difficulties = ["Easy", "Medium", "Hard"]

if choose_zone == "Forest":
    quest_name = "Lost Delivery"
    quest_description = "A local merchant has lost a valuable package and needs someone to find it.\
          The package is believed to have been dropped somewhere in the nearby forest.\
              Your task is to locate and retrieve the package and return it to the merchant.\
                  Be cautious of any creatures or obstacles you may encounter in the forest."
    quest_difficulty = "Easy"

if choose_zone == "Dungeon":
    pass

if choose_zone == "Jungle":
    pass

if choose_zone == "Desert":
    pass