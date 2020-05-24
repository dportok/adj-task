""" Basic tests for the CLI tool """
import adjust

numbers = list(range(1, 11))


def test_get_list_type():
    """ Make sure that you get a list with length of 10 """
    assert type(adjust.shuffle_numbers(numbers)) == list


def test_get_list_length():
    """ Make sure that the length of the resulted list is 10 """
    assert len(adjust.shuffle_numbers(numbers)) == 10


def test_number_occurence():
    """ Make sure that each number appears only one time """
    for i in numbers:
        assert adjust.shuffle_numbers(numbers).count(i) == 1
