# THE WARRIORS

class Warrior:
    health = 50
    attack = 5
    is_alive = True
    defence = 0
    attacks_dealt = 0

    def get_wounds(self, dmg):
        self.health -= dmg
        self.check_alive()
        return dmg

    def check_alive(self):
        if self.health <= 0:
            self.is_alive = False


class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):

    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defence = 2

    def get_wounds(self, dmg):
        if dmg > self.defence:
            self.health -= dmg-self.defence
            self.check_alive()
            return dmg-self.defence
        return 0


class Vampire(Warrior):

    vampirism = 0.5

    def __init__(self):
        super().__init__()
        self.attack = 4
        self.health = 40

    def lifesteal(self, defender):
        self.health += int((self.attack - defender.defence) * self.vampirism)


class Lancer(Warrior):
    second_target = [0, 0]

    def __init__(self):
        super().__init__()
        self.attack = 6
        self.health = 50

    # [0] - amount of attacks, [1] - damage
    def reset_sec_target(self):
        self.second_target = [0, 0]



def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        attack(unit_1, unit_2)
        if unit_2.is_alive:
            attack(unit_2, unit_1)
    return unit_1.is_alive


def attack(offender, defender):
    x = defender.get_wounds(offender.attack)
    if type(offender) is Vampire:
        offender.lifesteal(defender)
    elif type(offender) is Lancer:
        offender.second_target[0] += 1
        offender.second_target[1] += x


class Army:

    def __init__(self):
        self.list_warriors = []

    def add_units(self, unit_type, number):
        for x in range(0, number):
            self.list_warriors.append(unit_type())
        # print("I added " + str(len(self.list_warriors)) + " warriors")


class Battle:

    def fight(self, army1: Army, army2: Army):
        #print("battle start")
        while len(army1.list_warriors) != 0 and len(army2.list_warriors) != 0:
            fighters_health = (army1.list_warriors[0], army2.list_warriors[0] )
            if fight(army1.list_warriors[0], army2.list_warriors[0]):
                self.check_lancers(army1.list_warriors, army2.list_warriors)
                army2.list_warriors.pop(0)
            else:
                self.check_lancers(army1.list_warriors, army2.list_warriors)
                army1.list_warriors.pop(0)
        if len(army2.list_warriors) == 0:
            return True
        return False

    def check_lancers(self, list1, list2):
        if type(list1[0]) is Lancer and len(list2) > 1:
            self.lancer_dmg(list1, list2)
        if type(list2[0]) is Lancer and len(list1) > 1:
            self.lancer_dmg(list2, list1)

    def lancer_dmg(self, list_off, list_def):
        list_def[1].health -= (list_off[0].second_target[1] - list_def[1].defence * list_off[0].second_target[0])/2
        list_off[0].reset_sec_target()

"""
    def fight_solo(self, unit_1: Warrior, unit_2: Warrior):
        while unit_1.is_alive and unit_2.is_alive:
            attack(unit_1, unit_2)
            if unit_2.is_alive:
                attack(unit_2, unit_1)
        return unit_1.is_alive
"""

'''
MAIN
'''

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")