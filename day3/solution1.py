#!/usr/bin/env python3
"""Advent of Code 2025 - Day 3: Lobby"""


def max_joltage(bank: str) -> int:
    """
    Find the maximum 2-digit joltage from a bank.
    We need to pick 2 batteries (digits) in order to form the largest number.

    Strategy: Find the largest digit for the tens place, then find the largest
    digit after it for the ones place.
    """
    n = len(bank)
    max_val = 0

    # Try each pair of positions (i, j) where i < j
    for i in range(n - 1):
        for j in range(i + 1, n):
            val = int(bank[i] + bank[j])
            max_val = max(max_val, val)

    return max_val


def solve(input_text: str) -> int:
    """
    Sum the maximum joltage from each bank.
    """
    total = 0

    for line in input_text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        total += max_joltage(line)

    return total


def main():
    with open('day3/input.txt', 'r') as f:
        input_text = f.read()

    answer = solve(input_text)
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()
