# This is the first file in which I'm going to define all the characters and inputs that the players
# have to make to play the game.

# I am also storing the players initial information i.e. their names

class Character:
    def __init__(self, name, health, attack, attack_speed, defense, experience, level):
        self.name = name
        self.health = health
        self.attack = attack
        self.attack_speed = attack_speed
        self.defense = defense
        self.experience = experience
        self.level = level
        
    def gain_experience(self, xp):
         self.experience += xp

    def calculate_exp_threshold(self):
        #Defining a formula for XP threshold
        return self.level * 100 # Example: 100 XP needed for level 2, 200 XP needed for level 3 and so on.
    
    def level_up(self):
        self.level += 1
        if self.level % 1 == 0:
            self.attack += 1 # Increase attack every level

        if self.level % 2 == 0:
            self.health += 10
            self.defense += 5

        if self.level % 5 == 0:
            self.attack += 10
            self.attack_speed += 0.10


class Player:
    def __init__(self, name, character):
        self.name = name
        self.character = character

    def display_info(self):
        return f"{self.name}: {self.character.name} (Health: {self.character.health}, Attack: {self.character.attack}, AttackSpeed: {self.character.attack_speed} Defense: {self.character.defense})"

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

players = []
num_players = int(input("How many players are going to play the game? "))
initial_level_of_character = 1

for _ in range(num_players):
    player_name = input(f"Enter a Username {_ + 1}: ")
    character_name = input(f"{player_name}: Choose your character ({', '.join(character_dict.keys())}): ")

    while character_name not in character_dict:
        print("Please choose a valid character.")
        character_name = input(f"{player_name}: Choose your character ({', '.join(character_dict.keys())}): ")

    player_character = character_dict[character_name]
    players.append(Player(player_name, player_character))

for player in players:
    print(player.display_info())
    