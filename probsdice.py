import random


class Dice:
    def __init__(self):
        self.dice_side = 0

    def roll_dice(self):
        self.dice_side = random.randint(1, 6)
        return self.dice_side


if __name__ == "__main__":
    num_role = 3
    dice = Dice()
    rslt = []

    for a in range(num_role):
        rslt.append(dice.roll_dice())
    print(rslt)
