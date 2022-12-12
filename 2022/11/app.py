from functools import reduce
import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


class Monkey:
    def __init__(self, items, operation, test, throw_to, worried):
        self.common_divisor = None
        self.items = items
        self.operation = operation
        self.test = test
        self.throw_to = throw_to
        self.worried = worried
        self.items_inspected = 0

    def inspect(self):
        self.items_inspected += 1
        item = self.items.pop(0)
        item = self.perform_operation(item)
        if self.worried:
            item %= self.common_divisor
        else:
            item //= 3
        if item % self.test == 0:
            return item, self.throw_to[0]
        else:
            return item, self.throw_to[1]

    def perform_operation(self, item):
        if self.operation[0] == '*':
            if self.operation[1] == 'old':
                return item ** 2
            else:
                return item * int(self.operation[1])
        else:
            if self.operation[1] == 'old':
                return item + item
            else:
                return item + int(self.operation[1])


def get_monkey_business(rounds, worried):
    monkeys = []

    data = get_input('input/input.txt')
    while True:
        try:
            next(data)
            starting_items = [int(i) for i in next(data).split(': ')[1].split(', ')]
            operation = next(data).split()[-2:]
            test = int(next(data).split()[-1])
            throw_to = [int(next(data).split()[-1]), int(next(data).split()[-1])]
            monkeys.append(Monkey(starting_items, operation, test, throw_to, worried))
            next(data)
        except StopIteration:
            break

    if worried:
        divisors = []
        for monkey in monkeys:
            divisors.append(monkey.test)
        common_divisor = reduce(lambda x, y: x * y, divisors)
        for monkey in monkeys:
            monkey.common_divisor = common_divisor

    for i in range(rounds):
        for monkey in monkeys:
            while len(monkey.items) != 0:
                item, throw_to = monkey.inspect()
                monkeys[throw_to].items.append(item)

    items_inspected = sorted([monkey.items_inspected for monkey in monkeys])
    return items_inspected[-1] * items_inspected[-2]


def main():
    # Answer the first question: Level of monkey business
    answer(1, get_monkey_business(20, False))

    # Answer the second question: Level of worried monkey business
    answer(2, get_monkey_business(10000, True))


if __name__ == '__main__':
    main()
