import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


def find_non_repeating_sequence(data, length):
    for i in range(length - 1, len(data)):
        if len(set(data[i-length+1:i+1])) == length:
            return i + 1


def main():
    for data in get_input('input/input.txt'):
        # Answer the question: Where's the first start sequence?
        answer(1, find_non_repeating_sequence(data, 4))
        # Answer the question: Where's the first start sequence?
        answer(2, find_non_repeating_sequence(data, 14))


if __name__ == '__main__':
    main()
