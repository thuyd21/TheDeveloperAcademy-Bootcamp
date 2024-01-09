import random

class Dice:
    def __init__(self, min: int = 1, max: int = 6) -> None:
        self.min = min
        self.max = max

    def roll(self) -> None:
        while True:
            result = random.randint(self.min, self.max)
            print(f'Your roll is {result}')
            while True:
                reroll = input('Would you like to roll again (y/n)? ')
                reroll = reroll.lower()
                if reroll not in ('y', 'n'):
                    print('Please enter y/n.')
                    continue
                break
            if reroll == 'y':
                continue
            elif reroll == 'n':
                break

d6 = Dice()
d6.roll()