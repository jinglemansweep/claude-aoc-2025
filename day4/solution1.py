#!/usr/bin/env python3
"""Advent of Code 2025 - Day 4: Printing Department"""


def solve(input_text: str) -> int:
    """
    Count rolls of paper (@) that are accessible by forklifts.
    A roll is accessible if fewer than 4 of its 8 adjacent cells contain rolls.
    """
    lines = input_text.strip().split('\n')
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # 8 directions: up, down, left, right, and 4 diagonals
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]

    accessible_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                # Count adjacent rolls
                adjacent_rolls = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        adjacent_rolls += 1

                # Accessible if fewer than 4 adjacent rolls
                if adjacent_rolls < 4:
                    accessible_count += 1

    return accessible_count


def main():
    with open('day4/input.txt', 'r') as f:
        input_text = f.read()

    answer = solve(input_text)
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()
