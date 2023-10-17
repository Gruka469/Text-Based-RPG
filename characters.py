# This is the first file in which I'm going to define all the characters and inputs that the players
# have to make to play the game.

# I am also storing the players initial information i.e. their names

class Character:
    def __init__(self, name, health, attack, attack_speed, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.attack_speed = attack_speed
        self.defense = defense

class Player:
    def __init__(self, name, character):
        self.name = name
        self.character = character

    def display_info(self):
        return f"{self.name}: {self.character.name} (Health: {self.character.health},\
              Attack: {self.character.attack}, Defense: {self.character.defense})"

# Create a dictionary to map character names to Character instances
character_dict = {
    'Warrior': Character('Warrior', 610, 15, 1.00, 80),
    'Rogue': Character('Rogue', 520, 8, 1.18, 60),
    'Mage': Character('Mage', 450, 20, 0.80, 30),
    'Druid': Character('Druid', 480, 12, 1.03, 50),
    'Priest': Character('Priest', 400, 20, 0.80, 30),
    'Paladin': Character('Paladin', 650, 15, 0.90, 90),
    'Hunter': Character('Hunter', 500, 10, 1.10, 50),
    'Warlock': Character('Warlock', 450, 25, 0.75, 30),
    'Shaman': Character('Shaman', 550, 15, 1.00, 75)
}

start = input("Do you wanna play the game? y/n? ")
players = input("How many players are going to play the game? ")
list_players = players.split()
character = input("Each player must choose their character: ")




while players <= 9:
    character = input(f"{players}: Choose your character (Warrior, Rogue, Mage, etc.): ")

    if character == 'Warrior':
        print(f"{players}: You've selected {character} as your character.")
    elif character == 'Rogue':
        print(f"{players}: You've selected {character} as your character.")
    elif character == 'Mage':
        print(f"{players}: You've selected {character} as your character.")
    elif character == 'Druid':
        print(f"{players}: You've selected {character} as your character.")
    elif character == 'Preist':
        print(f"{players}: You've selected {character} as your character.")
    elif character == 'Paladin':
        print(f"{players}: You've selected {character} as your character.")
    elif character == 'Hunter':
        print(f"{players}: You've selected {character} as your character.")
    elif character == 'Warlock':
        print(f"{players}: You've selected {character} as your character.")
    elif character == 'Shaman':
        print(f"{players}: You've selected {character} as your character.")
    else:
        print("Please choose a valid character: ")
        continue
