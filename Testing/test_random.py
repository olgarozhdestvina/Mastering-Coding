import unittest
from RandomGame import random_game

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_random_game(self):
        answer, guess = 5, 5
        result = random_game.run_guess(answer, guess)
        self.assertTrue(result)

    def test_random_game2(self):
        answer, guess = 5, 3
        result = random_game.run_guess(answer, guess)
        self.assertFalse(result)

    def test_random_game3(self):
        answer, guess = 5, 'ghyt'
        result = random_game.run_guess(answer, guess)
        self.assertFalse(result)


    
if __name__ == '__main__':
    unittest.main()