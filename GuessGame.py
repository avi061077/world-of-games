from time import sleep


def generate_number(user_difficulty):
    # Will generate automatic random number
    import random
    secret_number = (random.randint(1, user_difficulty))
    return secret_number


def get_guess_from_user(user_difficulty):
    # The user will choose a number
    user_number = input(f"You need to guess a number between 1 to {user_difficulty}: ")
    if user_number.isdigit():
        return user_number


def compare_results(user_number, secret_number):
    # checking if the number the user chose equal to the random number
    if user_number or secret_number == type(int):
        if int(user_number) != int(secret_number):
            print("Wrong guess! The number was " + str(secret_number))
            user_win = False

        else:
            print("Well done you guessed the number!!!")
            user_win = True
            return user_win
    else:
        print("Error: You need to enter only numbers !!!"
              "please try again!!")


def play(user_difficulty):
    print("========  Welcome To GuessGame=========")
    # The start function, will start all functions and return false or true
    print("Generating a Number....")
    secret_number = generate_number(user_difficulty)
    sleep(2)
    user_number = get_guess_from_user(user_difficulty)
    sleep(1)
    guess_number = compare_results(user_number, secret_number)
    return guess_number
