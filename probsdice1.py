import random


class Dice:
    def __init__(self):
        self.dice_side = 0

    def roll_dice(self):
        self.dice_side = random.randint(1, 6)
        return self.dice_side


if __name__ == "__main__":
    num_rolls = 3
    dice = Dice()
    rslt = []
    trial_rolls = 5

    for a in range(trial_rolls):
        counts = 0
        list_dice = []
        for a in range(num_rolls):
            list_dice.append(dice.roll_dice())
            if list_dice[a] == 1:
                counts += 1

        if counts >= 1:
            rslt.append(1)
        else:
            rslt.append(0)
    print(rslt.count(1))
    print("probability getting 1 from three", rslt.count(1) / trial_rolls)
