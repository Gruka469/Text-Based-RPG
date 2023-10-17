start = input("Do you wanna play the game? y/n? ")
players = input("How many players are going to play the game? 1-4: ")
character = input("Each player must choose their character: ")

class characters:
    def __init__(self, name, health, attack, defense, agility):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.agility = agility
    
    def take_damage(self, damage):
        self.health -= damage

class Mage(character):
    def __init__(self, name):
        super().__init__(name, health = 450, attack = 20, attack_speed = 0.80, defense = 30)
        self.mana = 350

class Warrior(character):
    def __init__(self, name):
        super().__init__(name, health = 610, attack = 15, attack_speed = 1.00, defense = 80)
        self.rage = 100

class Rogue(character):
    def __init__(self, name):
        super().__init__(name, health = 520, attack = 8, attack_speed = 1.18, defense = 60)
        self.energy = 100

class Druid(character):
    def __init__(self, name):
        super().__init__(name, health = 480, attack = 12, attack_speed = 1.03, defense = 50)
        self.mana = 350
        self.rage = 100
        self.energy = 100

class Preist(character):
    def __init__(self, name):
        super().__init__(name, health = 400, attack = 20, attack_speed = 0.80, defense = 30)
        self.mana = 380

class Paladin(character):
    def __init__(self, name):
        super().__init__(name, health = 650, attack = 15, attack_speed = 0.90, defense = 90)
        self.mana = 330

class Hunter(character):
    def __init__(self, name):
        super().__init__(name, health = 500, attack = 10, attack_speed = 1.10, defense = 50)
        self.mana = 320

class Warlock(character):
    def __init__(self, name):
        super().__init__(name, health = 450, attack = 25, attack_speed = 0.75, defense = 30)
        self.mana = 380

class Shaman(character):
    def __init__(self, name):
        super().__init__(name, health = 550, attack = 15, attack_speed = 1.00, defense = 75)
        self.mana = 340

while character > 4 or character == "Done":
    character = input("Next character: ")

    if character == 'Warrior':
        pass
    elif character == 'Rogue':
        pass
    elif character == 'Mage':
        pass
    elif character == 'Druid':
        pass
    elif character == 'Preist':
        pass
    elif character == 'Paladin':
        pass
    elif character == 'Hunter':
        pass
    elif character == 'Warlock':
        pass
    elif character == 'Shaman':
        pass
    else:
        print("Please choose a valid character: ")
        continue
