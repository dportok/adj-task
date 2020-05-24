""" This program prints the numbers from 1 to 10 in random order """
import random

NUMBERS = list(range(1, 11))


def shuffle_numbers(number_list):
    """ Prints a shuffled version of the input number list """
    shuffled_list = number_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list


def main():
    """ Prints a shuffled version of the input number list """
    print(shuffle_numbers(NUMBERS))

if __name__ == "__main__":
    main()
