import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


win_against = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}
score_guide = {
    'win': 6, 'tie': 3, 'loss': 0,
    'Z': 6, 'Y': 3, 'X': 0,
    'A': 1, 'B': 2, 'C': 3,
}

def puzzle1(data1, data2):
    hand1 = data1
    hand2 = chr(ord(data2) - 23)  # Convert XYZ to ABC
    score = 0

    if hand1 == hand2:
        score += score_guide.get('tie')
    elif win_against.get(hand2) == hand1:
        score += score_guide.get('win')
    else:
        score += score_guide.get('loss')

    return score + score_guide.get(hand2)


def puzzle2(data1, data2):
    hand1, goal = data1, data2
    score = 0

    if score_guide.get(goal) == 3:  # We need to tie
        score += score_guide.get(hand1)
    elif score_guide.get(goal) == 0:  # We need to lose
        score += score_guide.get(win_against.get(hand1))
    else:  # We need to win
        score += score_guide.get(win_against.get(win_against.get(hand1)))

    return score + score_guide.get(goal)


def main():
    score_puzzle1 = 0
    score_puzzle2 = 0

    for data in get_input('input/input.txt'):
        data1, data2 = data.split()
        score_puzzle1 += puzzle1(data1, data2)
        score_puzzle2 += puzzle2(data1, data2)

    # Answer the first question: Your score assuming how the game works
    answer(1, score_puzzle1)

    # Answer the second question: Your score knowing how the game works
    answer(2, score_puzzle2)


if __name__ == '__main__':
    main()
