import random
import sys

class RandomGame:
    def run_guess(self, num, guess):
        if num == guess:
            print(f"Well done! It's {guess}!")
            return True
        return False

    def game(self):
        #start = int(sys.argv[1])
        #end = int(sys.argv[2])
        start = 1
        end = 20
        num = random.randint(start,end)

        try:
            c = 3
            guess = int(input(f'Guess a number between {start} and {end}. You have {c} attempts\nYour guess: '))
            while c !=1:
                if self.run_guess(num, guess):
                    break
                c -=1
                guess = int(input(f'Please try again. You have {c} attempts left\nYour guess: '))
        except ValueError as e:
            print(e)
        finally:
            return 'Game over'

random_game = RandomGame()
print(random_game.game())
