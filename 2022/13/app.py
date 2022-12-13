import json
from functools import cmp_to_key
import sys
sys.path.insert(0, '../../')
from utils.answer import answer
from utils.input import get_input


def compare(left, right):
    if type(left) == int and type(right) == int:
        if left == right:
            return None
        else:
            return left < right

    if type(left) == int: left = [left]
    if type(right) == int: right = [right]

    for i in range(min(len(left), len(right))):
        compared = compare(left[i], right[i])
        if compared is None:
            continue
        return compared

    if len(left) == len(right):
        return None
    return len(left) < len(right)


def main():
    packets = []
    data = get_input('input/input.txt')
    for value in data:
        packets.append((json.loads(value), json.loads(next(data))))
        next(data)

    # Answer 1
    score = 0
    for i, packet in enumerate(packets):
        if compare(*packet):
           score += i + 1
    answer(1, score)

    # Answer 2
    packets = [packet for packet_group in packets for packet in packet_group]
    packets.extend([[[2]], [[6]]])
    compare_cmp = cmp_to_key(lambda left, right: { True: 1, False: -1, None: 0 }.get(compare(left, right)))
    sorted_packets = sorted(packets, key=lambda x: compare_cmp(x), reverse=True)
    answer(2, (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))


if __name__ == '__main__':
    main()
