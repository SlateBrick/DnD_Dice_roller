import random as r

class dice_roller(object):

    results = []



    def __init__(self,rolls,sides):
        self.rolls = rolls
        self.sides = sides

        self.roll()

    def roll(self):
        self.roll_result = []
        for t in range(0,self.rolls):
            self.roll_result.append(r.randint(1,self.sides))


    def display(self):
        return f'd{self.sides} rolled {self.rolls} times with a result of {self.roll_result}'


x = dice_roller(3,20)


for i in range(0,10):
    print(x.display())
    x.roll()
