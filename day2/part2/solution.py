#!/usr/bin/env python3
"""Advent of Code 2025 - Day 2 Part 2: Gift Shop"""


def is_invalid_id(n: int) -> bool:
    """
    Check if a number is invalid (made of a sequence repeated at least twice).
    e.g., 55 (5x2), 111 (1x3), 6464 (64x2), 123123123 (123x3)
    """
    s = str(n)
    length = len(s)

    # Check all possible pattern lengths from 1 to length//2
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = length // pattern_len
            if repetitions >= 2 and pattern * repetitions == s:
                return True

    return False


def find_invalid_ids_in_range(start: int, end: int) -> list[int]:
    """
    Find all invalid IDs in a range.
    Generate potential invalid IDs and check if they fall within the range.
    """
    invalid_ids = set()

    start_len = len(str(start))
    end_len = len(str(end))

    # For each total length of the invalid ID
    for total_len in range(2, end_len + 1):
        if total_len < start_len:
            continue

        # For each possible pattern length that divides total_len
        for pattern_len in range(1, total_len // 2 + 1):
            if total_len % pattern_len != 0:
                continue

            repetitions = total_len // pattern_len
            if repetitions < 2:
                continue

            # Generate all possible patterns of this length
            if pattern_len == 1:
                pattern_start = 1
            else:
                pattern_start = 10 ** (pattern_len - 1)
            pattern_end = 10 ** pattern_len - 1

            for pattern_val in range(pattern_start, pattern_end + 1):
                pattern_str = str(pattern_val)
                invalid_id = int(pattern_str * repetitions)

                if start <= invalid_id <= end:
                    invalid_ids.add(invalid_id)

    return list(invalid_ids)


def solve(input_text: str) -> int:
    """
    Parse ranges and sum all invalid IDs found in them.
    """
    input_text = input_text.replace('\n', '').strip()

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
    with open('day2/part2/input.txt', 'r') as f:
        input_text = f.read()

    answer = solve(input_text)
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()
