import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


class CraneMover:
    def __init__(self):
        self.stacks = [[], [], [], [], [], [], [], [], []]

    def initialize_data(self, data):
        [self.stacks[i].append(cargo) for i, cargo in enumerate(data[1::4]) if cargo != ' ']

    def complete_initialization(self):
        [stack.pop() for stack in self.stacks if len(stack) > 0]
        [stack.reverse() for stack in self.stacks]

    def get_top_crates(self):
        return ''.join([stack[-1] for stack in self.stacks if len(stack) > 0])


class CraneMover9000(CraneMover):
    def move(self, amount, from_s, to_s):
        self.stacks[to_s - 1].extend([self.stacks[from_s - 1].pop() for _ in range(amount)])


class CraneMover9001(CraneMover):
    def move(self, amount, from_s, to_s):
        self.stacks[to_s - 1].extend([self.stacks[from_s - 1].pop() for _ in range(amount)][::-1])


def main():
    crane_movers = [CraneMover9000(), CraneMover9001()]
    are_we_receiving_moves = False
    for data in get_input('input/input.txt', do_strip=False):
        if data == '\n':
            are_we_receiving_moves = True
            [crane_mover.complete_initialization() for crane_mover in crane_movers]
        elif are_we_receiving_moves:
            [crane_mover.move(*[int(i) for i in data.split()[1::2]]) for crane_mover in crane_movers]
        else:
            [crane_mover.initialize_data(data) for crane_mover in crane_movers]

    # Answer the questions: Which crates are on top?
    [answer(i + 1, crane_mover.get_top_crates()) for i, crane_mover in enumerate(crane_movers)]


if __name__ == '__main__':
    main()
