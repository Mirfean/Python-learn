import math

class BasicClass:

    def __init__(self):
        print("Hello there!")

    x = 15
    y = 4
    name = "Papryk"
    surname = "Kaczka"

    def add_things(self, x1, x2):
        return self.x + x1 + x2

    def first_code(self):
        print("General Kenobi!")

        print(type(self.x))
        print()
        print(self.add_things(self.name, self.surname))
        print(self.add_things(str(self.x), self.name))

    def collatz(self, number):
        if number % 2 == 0:
            print((number // 2))
            return number // 2
        elif number % 2 != 0:
            print((3 * number + 1))
            return 3 * number + 1

    def diffLists(self):
        mylist = []

        mytuple = (1, 2, 3)
        mySingletuple = (1,)

        myset = {1, 2, 3}
        myset2 = set()

        myDictionary = {1: 'apple', 2: 'ball'}

    def main01(self):
        superList = [self.add_things(15, 15), self.add_things(11, 11), self.add_things(2, 2)]
        print(superList)

        firstString = "I love {0} and {1}".format("foxes", "curry")
        print(firstString)
        print("str[2:7] " + firstString[2:7])
        print("str[:8] " + firstString[:8])
        print("str[2:7:15] " + firstString[2:7:15])
        print(math.pi)
        print(eval('2+3'))

        value = input("Give me a value! ")
        print("Yo man, you really just wrote {0}? That's a cringe, dude".format(str(value)))

        list1 = [1, 2, 3]
        list2 = [1, 2, 3]

        print("choose a number:")
        n = int(input())
        while n != 1:
            n = self.collatz(int(n))

        # should be true
        print("should be true " + str(list1 == list2))
        # should be false
        print("should be false " + str(list1 is list2))

        if 1 in list1:
            print("Elo 1")

        for elo in range(0, 10):
            print(elo)
        else:
            print("End of FOR")

        polo = 15
        while polo > 10:
            print("disco {xpolo}".format(xpolo=polo))
            polo -= 1

        print("2->20 each 3")
        print(list(range(2, 20, 3)))

        t = True
        f = False

        print('x and y is', t and f)
        print('x or y is', t or f)
        print('not x is', not t)
