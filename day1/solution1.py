#!/usr/bin/env python3
"""Advent of Code 2025 - Day 1: Secret Entrance"""


def solve(input_text: str) -> int:
    """
    Solve the puzzle: count how many times the dial lands on 0.

    - Dial has numbers 0-99
    - Starts at 50
    - L = rotate left (subtract), R = rotate right (add)
    - Wraps around (0-1 = 99, 99+1 = 0)
    """
    position = 50
    zero_count = 0

    for line in input_text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        if direction == 'L':
            position = (position - distance) % 100
        else:  # R
            position = (position + distance) % 100

        if position == 0:
            zero_count += 1

    return zero_count


def main():
    with open('day1/input.txt', 'r') as f:
        input_text = f.read()

    answer = solve(input_text)
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()
