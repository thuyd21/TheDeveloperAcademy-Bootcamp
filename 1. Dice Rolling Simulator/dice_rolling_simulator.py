import random

class Dice:
    def __init__(self, min: int = 1, max: int = 6) -> None:
        self.min = min
        self.max = max

    def roll(self) -> None:
        while True:
            result = random.randint(self.min, self.max)
            print(f'Your roll is {result}')
            reroll = self._reroll()
            if not reroll:
                break
    
    def _reroll(self) -> bool:
        while True:
            confirm = ['y']
            deny = ['n']
            user_input = input(f'Would you like to roll again ({confirm[0]}/{deny[0]})? ')
            decision = user_input.lower()
            if decision in confirm:
                return True
            if decision in deny:
                return False
            print(f'Please enter {confirm[0]}/{deny[0]}.')

d6 = Dice()
d6.roll()