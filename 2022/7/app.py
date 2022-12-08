import string
import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


def main():
    directories = { }
    current_directory_array = []

    for data in get_input('input/input.txt'):
        if data[0] == '$':  # Command
            if data[2:4] == 'cd':  # Change directory
                directory = data.split()[-1]
                if directory == '..':
                    current_directory_array.pop()
                else:
                    current_directory_array.append(directory)
        elif data[0] in string.digits:
            size = int(data.split()[0])
            for i in range(len(current_directory_array)):
                directory = '/' + '/'.join(current_directory_array[1:i+1])
                directories[directory] = directories.get(directory, 0) + size

    total_disk_space = 70000000
    disk_space_needed = 30000000
    current_disk_space_used = directories['/']
    disk_space_required = -(total_disk_space - disk_space_needed - current_disk_space_used)

    sum_smaller_than_100000 = 0
    smallest_size_large_enough_to_fix_problem = current_disk_space_used
    for directory, size in directories.items():
        # All directories smaller than 10000
        if size < 100000:
            sum_smaller_than_100000 += size
        # Smallest directory large enough to fix the problem
        if smallest_size_large_enough_to_fix_problem > size > disk_space_required:
            smallest_size_large_enough_to_fix_problem = size

    # Answer the first question: What's the sum of the directories smaller than 100000?
    answer(1, sum_smaller_than_100000)
    # Answer the second question: What's the size of the directory to remove?
    answer(2, smallest_size_large_enough_to_fix_problem)


if __name__ == '__main__':
    main()
