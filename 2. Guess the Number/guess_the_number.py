import random

class GuessingGame:
    def __init__(self, min: int = 1, max: int = 100) -> None:
        self.min = min
        self.max = max
    
    def run(self) -> None:
        print(f'Generating a number from {self.min} to {self.max}.')
        number = random.randint(self.min, self.max)
        while True:
            try:
                guess = input('What is the number? ')
                guess = int(guess)
            except ValueError:
                print('Please enter an integer.')
                continue
            if guess < number:
                print('Too low.')
            elif guess > number:
                print('Too high.')
            else:
                print('You Win!')
                break

game = GuessingGame()
game.run()