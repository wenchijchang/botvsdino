class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot): # reduce robot health
        robot.health -= self.attack_power
        print(f'{self.name} attacked {robot.name} for {self.attack_power} damage!\n{robot.name} has {robot.health} remaining!')
