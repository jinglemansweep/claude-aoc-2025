#!/usr/bin/env python3
"""Advent of Code 2025 - Day 3 Part 2: Lobby"""


def max_joltage_12(bank: str) -> int:
    """
    Find the maximum 12-digit joltage from a bank.
    We need to pick exactly 12 batteries (digits) in order to form the largest number.

    Greedy approach: For each of the 12 positions, pick the largest available digit
    that still leaves enough digits remaining for the rest of the positions.
    """
    n = len(bank)
    k = 12  # number of digits to pick

    result = []
    start = 0

    for i in range(k):
        # We need to pick (k - i) more digits including this one
        # So we can look from 'start' up to index (n - (k - i))
        remaining_needed = k - i
        end = n - remaining_needed  # last valid index to pick from

        # Find the maximum digit in range [start, end]
        best_idx = start
        best_digit = bank[start]
        for j in range(start, end + 1):
            if bank[j] > best_digit:
                best_digit = bank[j]
                best_idx = j

        result.append(best_digit)
        start = best_idx + 1  # next digit must come after this one

    return int(''.join(result))


def solve(input_text: str) -> int:
    """
    Sum the maximum 12-digit joltage from each bank.
    """
    total = 0

    for line in input_text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        total += max_joltage_12(line)

    return total


def main():
    with open('day3/input.txt', 'r') as f:
        input_text = f.read()

    answer = solve(input_text)
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()
