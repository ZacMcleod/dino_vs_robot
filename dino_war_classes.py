import random

class Battlefield:
    def __init__(self):
        self.robot = Robot
        self.dinosaur = Dinosaur

    def run_game(self):
        Robot.name = input('''What is your name?: ''')
        Robot.active_weapon = input(f'''What Weapon will you wield?

        {list(list(Weapon.name))}: ''')

    def welcome(self):
        print('''POV: You are an A.I. ROBOT built for battle by aliens in the year 266 Universal Time.
        It is now the year 281 and the aliens have sent you to take over planet 0027, G, sector 141BG..
        AKA, "Earth". These earthlings seem pretty Over-Powered...''')

    def battle(self):
        pass

    def winner(self):
        pass

class Robot:
    def __init__(self, name):
        self.name = ''
        self.health = 200
        self.active_weapon = str(Weapon.name)
    def attack(self, dinosaur):
        dinosaur.health -= Weapon.attack_power
        print(f'You have dealt {Weapon.attack_power} to the Dinosaur')

class Dinosaur:
    def __init__(self, attack_power):
        self.name = ''
        self.attack_power = 30
        self.health = random.randint(20, 100)
    def attack(self, robot):
        robot.health -= self.attack_power

class Weapon:
    def __init__(self, attack_power):
        self.name = {
            'laser ponter': 3,
            'loose cords': 29,
            'nerf gun': 85,
            'oil shoes': 0,
            'drum stick': -31
        }
        self.attack_power = list(self.name.values)

