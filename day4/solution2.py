#!/usr/bin/env python3
"""Advent of Code 2025 - Day 4 Part 2: Printing Department"""


def solve(input_text: str) -> int:
    """
    Keep removing accessible rolls until none are accessible.
    Return the total number of rolls removed.
    """
    lines = input_text.strip().split('\n')
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # 8 directions: up, down, left, right, and 4 diagonals
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]

    def count_adjacent_rolls(r, c):
        """Count rolls adjacent to position (r, c)."""
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                count += 1
        return count

    def find_accessible_rolls():
        """Find all rolls that are currently accessible (fewer than 4 adjacent rolls)."""
        accessible = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    if count_adjacent_rolls(r, c) < 4:
                        accessible.append((r, c))
        return accessible

    total_removed = 0

    while True:
        accessible = find_accessible_rolls()
        if not accessible:
            break

        # Remove all accessible rolls
        for r, c in accessible:
            grid[r][c] = '.'

        total_removed += len(accessible)

    return total_removed


def main():
    with open('day4/input.txt', 'r') as f:
        input_text = f.read()

    answer = solve(input_text)
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()
