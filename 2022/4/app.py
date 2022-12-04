import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input

def do_ranges_fully_overlap(a_min, a_max, b_min, b_max):
    return (a_min <= b_min and a_max >= b_max) or (b_min <= a_min and b_max >= a_max)


def do_ranges_overlap(a_min, a_max, b_min, b_max):
    return (a_min <= b_min <= a_max) or (b_min <= a_min <= b_max)

def main():
    duplicate_pairs = 0
    overlapping_pairs = 0
    for data in get_input('input/input.txt'):
        elf1, elf2 = data.split(',')
        elf1_min, elf1_max = [int(i) for i in elf1.split('-')]
        elf2_min, elf2_max = [int(i) for i in elf2.split('-')]
        if do_ranges_fully_overlap(elf1_min, elf1_max, elf2_min, elf2_max):
            duplicate_pairs += 1
        if do_ranges_overlap(elf1_min, elf1_max, elf2_min, elf2_max):
            overlapping_pairs += 1


    # Answer the first question: How many assignment pairs fully contain the other?
    answer(1, duplicate_pairs)

    # Answer the second question: How many assignment pairs overlap with the other?
    answer(2, overlapping_pairs)


if __name__ == '__main__':
    main()
