from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("Godzilla", 25)
        self.robot = Robot("ZGMF-X10A Freedom Gundam")

    def greeting(self):
        print("""
        Welcome to Robot versus Dinosaur!Let the battle begin!
        """)

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
        

    def display_winner(self):
        print(f'''
        {self.robot.name} made {self.dinosaur.name} extinct! {self.robot.name} is the winner!''')


    def run_game(self):
        self.greeting()
        self.battle_phase()
        self.display_winner()