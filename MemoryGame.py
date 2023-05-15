import time
import random


def _generate_sequence(length_list):
    # Generate  Random numbers, creates a list and prints it
    random_numbers_list = []
    for number in range(0, length_list):
        user_number = random.randint(1, 101)
        random_numbers_list.append(user_number)
    while True:
        print(random_numbers_list, end="")
        time.sleep(0.7)
        print("", end="\r")
        break
    return random_numbers_list


def _get_list_from_user(length_list_user):
    user_numbers_list = []
    try:
        for i_list in range(0, length_list_user):
            user_input_numbers = input(f'Please enter your # {i_list + 1} number ')
            while not (user_input_numbers.isdigit()):
                break
            user_input_numbers = int(user_input_numbers)
            user_numbers_list.append(user_input_numbers)
        return user_numbers_list
    except  ValueError:
        print("Error: You need to enter only numbers !!!"
              "please try again!!")


def _is_list_equal(random_numbers_list, user_numbers_list):
    if random_numbers_list == user_numbers_list:
        equal = True
        print("Wow! you are amazing!! You Win!!!")
        print("The numbers were: ", random_numbers_list)
    else:
        print("You didn't guess the numbers... Don't give up, you can try again at any time!")
        print("The numbers were: ", random_numbers_list)
        equal = False
    return equal


def play(user_difficulty):
    print("========Welcome To Memory Game lets start..=========")
    random_list = _generate_sequence(user_difficulty)
    user_numbers_list = _get_list_from_user(user_difficulty)
    user_win = _is_list_equal(random_list, user_numbers_list)
    return user_win






