import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


def main():
    elves = []
    elf_counter = 1

    for data in get_input('input/input.txt'):
        if data == '':  # An empty line signifies a new elf
            elf_counter += 1
        else:  # When we have an amount of calories
            number = int(data)
            if elf_counter >= len(elves):  # If this elf is not yet tracked in the list
                elves.append((elf_counter, number))
            else:  # This elf is already in the list
                elves[elf_counter] = (elf_counter, elves[elf_counter][1] + number)

    # Sort the elves based from high to low based the amount of calories they're carrying
    elves.sort(key=lambda elf: elf[1], reverse=True)

    # Answer the first question: How many calories does the elf with the most calories carry
    answer(1, elves[0][1])

    # Get the top 3 elves
    top_elves_calories = sum([elf[1] for elf in elves[:3]])

    # Answer the second question: How many calories do the 3 elves with the most calories carry
    answer(2, top_elves_calories)


if __name__ == '__main__':
    main()
