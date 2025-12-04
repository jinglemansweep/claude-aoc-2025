#!/usr/bin/env python3
"""Advent of Code 2025 - Day 2: Gift Shop"""


def is_invalid_id(n: int) -> bool:
    """
    Check if a number is invalid (made of a sequence repeated twice).
    e.g., 55 (5+5), 6464 (64+64), 123123 (123+123)
    """
    s = str(n)
    length = len(s)

    # Must have even length to be a repeated sequence
    if length % 2 != 0:
        return False

    half = length // 2
    return s[:half] == s[half:]


def find_invalid_ids_in_range(start: int, end: int) -> list[int]:
    """
    Find all invalid IDs in a range.
    Instead of iterating through all numbers, we generate potential invalid IDs
    and check if they fall within the range.
    """
    invalid_ids = []

    # Determine the digit lengths we need to check
    # An invalid ID has even length, so we check lengths 2, 4, 6, 8, ...
    start_len = len(str(start))
    end_len = len(str(end))

    for total_len in range(2, end_len + 1, 2):
        if total_len < start_len:
            continue

        half_len = total_len // 2

        # Generate all possible "half" values
        # For half_len digits, range is 10^(half_len-1) to 10^half_len - 1
        # Exception: for half_len=1, range is 1-9
        if half_len == 1:
            half_start = 1
        else:
            half_start = 10 ** (half_len - 1)
        half_end = 10 ** half_len - 1

        for half_val in range(half_start, half_end + 1):
            # Create the invalid ID by repeating the half value
            half_str = str(half_val)
            invalid_id = int(half_str + half_str)

            if start <= invalid_id <= end:
                invalid_ids.append(invalid_id)

    return invalid_ids


def solve(input_text: str) -> int:
    """
    Parse ranges and sum all invalid IDs found in them.
    """
    # Parse the input - it's comma-separated ranges on potentially multiple lines
    input_text = input_text.replace('\n', '').strip()

    # Remove trailing comma if present
    if input_text.endswith(','):
        input_text = input_text[:-1]

    ranges = input_text.split(',')

    total = 0
    for range_str in ranges:
        range_str = range_str.strip()
        if not range_str:
            continue

        start, end = map(int, range_str.split('-'))
        invalid_ids = find_invalid_ids_in_range(start, end)
        total += sum(invalid_ids)

    return total


def main():
    with open('day2/input.txt', 'r') as f:
        input_text = f.read()

    answer = solve(input_text)
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()
