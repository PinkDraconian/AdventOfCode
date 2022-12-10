import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


class HandheldDevice:
    def __init__(self):
        self.cycle_data = []
        self.x = 1
        self.drawing = ''

    def run_cycle(self, difference):
        self.draw()
        self.x += difference
        self.cycle_data.append(self.x)

    def draw(self):
        if len(self.cycle_data) % 40 in range(self.x - 1, self.x + 2):
            self.drawing += '#'
        else:
            self.drawing += '.'


def main():
    handheld_device = HandheldDevice()
    for instruction in get_input('input/input.txt'):
        if instruction == 'noop':
            handheld_device.run_cycle(0)
        elif instruction[:4] == 'addx':
            handheld_device.run_cycle(0)
            handheld_device.run_cycle(int(instruction.split()[1]))

    signal_strengths = sum([handheld_device.cycle_data[i-2] * i \
                            for i in [20, 60, 100, 140, 180, 220]])

    # Answer the first question: Sum of the signal strengths
    answer(1, signal_strengths)
    # Answer the second question: What's the drawing?
    answer(2, 'See below')
    for i, character in enumerate(handheld_device.drawing):
        if i % 40 == 0 and i != 0:
            print()
        print(character, end='')


if __name__ == '__main__':
    main()
