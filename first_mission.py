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


def explore_forest_alone_first():
    print("You decide to venture into the forest alone to find the lost package.\
                It's a straightforward and perhaps quicker path.\
                You equip your gear and head into the dense woods, hoping to find the package without any distractions.")
    print("As you venture into the forest alone, the dense woods make it challenging to navigate. "
          "You'll have to rely on your survival skills and wits. Soon, you encounter a fork in the path. "
          "What do you do?")
    print("Choice 1: Take the left path, which seems to lead deeper into the forest.")
    print("Choice 2: Take the right path, which appears to lead to a clearing.")
    print("Choice 3: Set up camp for the night and continue your search in the morning.")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("You decide to take the left path, which leads you deeper into the forest. The darkness is overwhelming, "
              "and strange sounds surround you. You press on, hoping to find the package.")
        # Continue the story with more choices and outcomes based on the left path.

    elif choice == "2":
        print("You choose the right path, which leads to a clearing with a tranquil stream. You take a moment to rest "
              "and drink from the stream before continuing your search.")
        # Continue the story with more choices and outcomes based on the right path.

    elif choice == "3":
        print("You decide to set up camp for the night, hoping that resting will prepare you for the challenges ahead. "
              "As you gather firewood and set up your tent, you can't shake the feeling that you're being watched.")
        # Continue the story with more choices and outcomes based on setting up camp.

def seek_help_from_tracker_guild():
    print("Realizing that the forest can be dangerous, you decide to seek the help of the Tracker Guild in town.\
                    They are known for their exceptional skills in locating lost items and navigating the woods.\
                    You offer them a portion of the reward in exchange for their assistance.")
    print("You head back to town and find the Tracker Guild. They agree to help you for the promised reward.\
           The experienced tracker, Sarah, leads the way.\
           While you're safer with her guidance, it will cost you some of the reward.\
           Along the journey, you come across a river. What's your next move?")
    print("Choice 1: Attempt to cross the river, risking danger but saving time.")
    print("Choice 2: Ask Sarah for advice on the best way to navigate the river safely.")
    print("Choice 3: Decide to find an alternative route to avoid the river entirely.")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("You attempt to cross the river, facing danger but saving time.")
    elif choice == "2":
        print("You ask Sarah for advice on navigating the river safely.")
    elif choice == "3":
        print("You decide to find an alternative route to avoid the river entirely.")

def investigate_merchant_shop():
    print("Instead of heading straight to the forest, you decide to investigate the merchant's shop more thoroughly.\
                    You wonder if the package might not have even left the shop in the first place.\
                    You talk to the merchant, check the shop, and question any potential witnesses.")
    print("You begin to search the merchant's shop more thoroughly.\
           While examining the shelves, you discover a hidden compartment behind some crates.\
           Inside, you find a note suggesting that the package might have been stolen by a rogue employee.\
           What do you do next?")
    print("Choice 1: Confront the merchant with the evidence you've found.")
    print("Choice 2: Investigate the whereabouts of the rogue employee and attempt to retrieve the package.")
    print("Choice 3: Ignore the note and proceed with your original plan to search the forest, believing the note might be a distraction.")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("You confront the merchant with the evidence you've found.")
    elif choice == "2":
        print("You investigate the whereabouts of the rogue employee and attempt to retrieve the package.")
    elif choice == "3":
        print("You decide to ignore the note and proceed with your original plan to search the forest.")


def first_quests():
        random_key = random.choice(list(first_quest_choices))
        selected_choice = first_quest_choices[random_key]

        quest_name = "Lost Delivery"
        quest_description = "A local merchant has lost a valuable package and needs someone to find it.\
            The package is believed to have been dropped somewhere in the nearby forest.\
                Your task is to locate and retrieve the package and return it to the merchant.\
                    Be cautious of any creatures or obstacles you may encounter in the forest."
        quest_difficulty = "Easy"

        if selected_choice == 1:
            explore_forest_alone_first()
        elif selected_choice == 2:
            seek_help_from_tracker_guild()
        elif selected_choice == 3:
            investigate_merchant_shop()

if choose_zone == "Dungeon":
    pass

if choose_zone == "Jungle":
    pass

if choose_zone == "Desert":
    pass