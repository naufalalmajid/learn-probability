import random


class Dice:
    def __init__(self):
        self.dice_side = 0

    def roll_dice(self):
        self.dice_side = random.randint(1, 6)
        return self.dice_side


if __name__ == "__main__":
    num_dice = 3
    num_trial = 5
    rslt_dice = []

    for a in range(num_dice):
        rslt_dice.append(Dice())

    rslt_side = []

    for a in range(num_trial):
        roll = []
        for side in rslt_dice:
            roll.append(side.roll_dice())
        rslt_side.append(roll)

    print(rslt_side)
