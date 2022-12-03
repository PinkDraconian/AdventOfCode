import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


def get_priority(letter):
    priority = ord(letter.lower()) - 96
    if not letter.islower():
        priority += 26
    return priority


def main():
    total_priorities_common_item = 0
    total_priorities_group_item = 0
    groups = [[]]

    for rucksack in get_input('input/input.txt'):
        middle_length = len(rucksack) // 2
        compartment1, compartment2 = rucksack[:middle_length], rucksack[middle_length:]

        common_items = set(compartment1) & set(compartment2)
        total_priorities_common_item += get_priority(common_items.pop())

        if len(groups[-1]) < 3:
            groups[-1].append(rucksack)
        else:
            groups.append([rucksack])

    for group in groups:
        common_group_item = set(group[0])
        for rucksack in group[1:]:
            common_group_item = common_group_item & set(rucksack)
        total_priorities_group_item += get_priority(common_group_item.pop())

    # Answer the first question: The sum of priorities of common item in each rucksack
    answer(1, total_priorities_common_item)

    # Answer the first question: The sum of priorities of common item in each group
    answer(2, total_priorities_group_item)


if __name__ == '__main__':
    main()
