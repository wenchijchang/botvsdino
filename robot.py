from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Ultracompact Nuclear Fission Reactor", 40)

    def attack(self, dinosaur): # reduce dino health
        dinosaur.health -= self.active_weapon.attack_power
        if dinosaur.health > 0:
            print(f'{self.name} attacked {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage!\n{dinosaur.name} has {dinosaur.health} remaining!')
        else:
            print(f'{self.name} attacked {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage!\n{dinosaur.name} has 0 health remaining!')