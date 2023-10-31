from characters import Character
import random

choose_zone = input("Choose your zone: ")
zones = ["Forest", "Dungeon", "Jungle", "Desert"]
quest_difficulties = ["Easy", "Medium", "Hard"]
first_quest_choices = {
    1: "Explore the Forest Alone",
    2: "Seek Help from the Tracker Guild",
    3: "Investigate the Merchant's Shop"
}


def first_quests():
        random_key = random.choice(list(first_quest_choices))
        selected_choice = first_quest_choices[random_key]

        if selected_choice == 1:
             print("You decide to venture into the forest alone to find the lost package.\
                    It's a straightforward and perhaps quicker path.\
                    You equip your gear and head into the dense woods, hoping to find the package without any distractions.")
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