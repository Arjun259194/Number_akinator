import os
from random import randrange as rr
from time import sleep


class Game:
    def __init__(self):
        self.count = 0

    def start_game(self):
        for x in range(1, 4):
            os.system('CLS')
            print('Guess a number from 1 to 100')
            print(f'Game will start in... {x}')
            sleep(1)
        print('game starting'.upper())
        sleep(2)
        self.game(1,101)

    def get_user_input(self, number):
        print(
            'Y : yes',
            'G : greater then your number',
            'L : less then your number',
            sep='\n'
        )
        print(f'\nIs your guessed number {number}?\n')
        return input('Enter your input:')

    def game(self, min, max):
        os.system('CLS')
        computer_guess = rr(min, max+1)
        user_input = self.get_user_input(computer_guess).upper()

        if user_input == 'Y':
            self.final_result()
        elif user_input == 'G':
            self.count += 1
            self.game(min, computer_guess)
        elif user_input == 'L':
            self.count += 1
            self.game(computer_guess, max)
        else:
            print('input not write try again')

    def final_result(self):
        if self.count <= 10:
            print('i am Genius!!!! XD'.upper())
        elif self.count <= 20:
            print('Not that bad i think :]'.capitalize())
        elif self.count > 20:
            print('You won... :[')
        else:
            print('you won')
        
        sleep(3)
        os.system('CLS')
        exit()

game = Game()
game.start_game()