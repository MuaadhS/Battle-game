import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, hp, mp, atk, df, mag):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.mag = mag
        self.actions = ["Attack", "Magic"]

    def damage(self):
        return random.randrange(self.atkl, self.atkh)

    def spelldamage(self, i):
        mgl = self.mag[i]["damage"] - 5
        mgh = self.mag[i]["damage"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.mag[i]["name"]

    def get_spell_mp(self, i):
        return self.mag[i]["cost"]

    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC )
        for item in self.actions:
            print(str(i) + ":", item)
            i+=1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Magic" + bcolors.ENDC )
        for spell in self.mag:
            print(str(i) + ":", spell["name"], "(cost: ", str(spell["cost"]) + ")")
            i+=1
