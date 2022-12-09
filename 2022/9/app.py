import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


def display(knots):
    for i in range(-11, 11):
        for j in range(-11, 11):
            try:
                print(knots.index((j, i)), end='')
            except ValueError:
                print('.', end='')
        print()


direction_mapping = {
    'R': (1, 0), 'L': (-1, 0),
    'U': (0, -1), 'D': (0, 1)
}


def sign(x):
    return 1 if x >= 0 else -1


def move(knot, direction):
    return knot[0] + direction[0], knot[1] + direction[1]


def follow(head, tail):
    if abs(head[0] - tail[0]) > 1:
        if abs(head[1] - tail[1]) >= 1:  # If diagonal
            tail = move(tail, (sign(head[0] - tail[0]), sign(head[1] -tail[1])))
        else:  # Move straight
            tail = move(tail, (sign(head[0] - tail[0]), 0))
    elif abs(head[1] - tail[1]) > 1:
        if abs(head[0] - tail[0]) >= 1:  # If diagonal
            tail = move(tail, (sign(head[0] - tail[0]), sign(head[1] - tail[1])))
        else:  # Move straight
            tail = move(tail, (0, sign(head[1] - tail[1])))
    return tail


def calculate_rope(knots):
    knots = [(0, 0)] * knots
    tail_history = []
    for step in get_input('input/input.txt'):
        direction, amount = step.split()
        direction = direction_mapping.get(direction)
        amount = int(amount)

        for _ in range(amount):
            knots[0] = move(knots[0], direction)
            for i in range(1, len(knots)):
                knots[i] = follow(knots[i-1], knots[i])
            tail_history.append(knots[-1])
    return len(set(tail_history))


def main():
    # Answer the first question: How many tiles does the tail visit?
    answer(1, calculate_rope(2))
    # Answer the second question:
    answer(2, calculate_rope(10))


if __name__ == '__main__':
    main()
