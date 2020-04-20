import random as r

class dice_roller(object):

    """
    create a object with a list of random values defined by the number
    'rolls' and how many 'sides' there are
    """

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


"""
example of a dice_roller object with 20 sides rolled 3 times
"""
# x = dice_roller(3,20)
#
#
# for i in range(0,10):
#     print(x.display())
#     x.roll()
