# THE WARRIORS

class Warrior:
    HP = 50
    Attack = 5
    is_alive = True

    def check_alive(self):
        if self.HP <= 0:
            self.is_alive = False


class Knight(Warrior):
    Attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        attack(unit_1, unit_2)
        if unit_2.is_alive:
            attack(unit_2, unit_1)
    return unit_1.is_alive


def attack(offender, defender):
    defender.HP -= offender.Attack
    defender.check_alive()
# /THE WARRIORS


'''
MAIN
'''

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