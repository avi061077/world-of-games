import GuessGame
import CurrencyRouletteGame
import MemoryGame
from Score import add_score


def welcome(name):
    return f"""
Hello {name} and welcome to the World of Games (WoG)
Here you can find many cool games to play."""


user_input = input("Hello, please enter your name ")
user_output = welcome(user_input)


def load_game():
    user_choose = input("""
    Please choose a game to play:
    1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2.Guess Game - guess a number and see if you chose like the computer
    3.Currency Roulette - try and guess the value of a random amount of USD in ILS
    > """)
    if user_choose.isdigit():
        user_choose_game = int(user_choose)
        if user_choose_game > 3:
            print("you put wrong number please choose game number between 1-3")

        else:
            user_difficulty = input("Please choose game difficulty from 1 to 5:")
            if user_difficulty.isdigit():
                user_difficulty_choose = int(user_difficulty)
                if user_difficulty_choose > 5:
                    print("you put wrong numer please choose game number between 1-5")
                # Calling Game number one (Memory Game)
                elif user_choose_game == 1:
                    while True:
                        MemoryGame.play(int(user_difficulty))
                        MemoryGame_user_input = input("want to play again? (Y)yes or (N)no  ")
                        if MemoryGame_user_input.upper() == 'Y':
                            MemoryGame.play(int(user_difficulty))
                            add_score(difficulty=user_difficulty_choose)
                        else:
                            print("Thank you for playing GuessGame ")
                            break

                # Calling Game number Two (GuessGame)
                elif user_choose_game == 2:
                    while True:
                        GuessGame.play(int(user_difficulty))
                        GuessGame_user_input = input("want to play again? (Y)yes or (N)no  ")
                        if GuessGame_user_input.upper() == 'Y':
                            GuessGame.play(int(user_difficulty))
                            add_score(difficulty=user_difficulty_choose)
                        else:
                            print("Thank you for playing GuessGame ")
                            break

                # Calling Game number Three (CurrencyRouletteGame)
                elif user_choose_game == 3:
                    CurrencyRouletteGame.play(int(user_difficulty))
                    while True:
                        CurrencyRouletteGame.play(int(user_difficulty))
                        CurrencyRouletteGame_user_input = input("want to play again? (Y)yes or (N)no  ")
                        if CurrencyRouletteGame_user_input.upper() == 'Y':
                            CurrencyRouletteGame.play(int(user_difficulty))
                            add_score(difficulty=user_difficulty_choose)
                        else:
                            print("Thank you for playing CurrencyRouletteGame ")
                            break


            else:
                print('Incorrect data ,Please enter a number between 1 and 5')

    else:
        print('Incorrect data ,Please enter a number between 1 and 3')
