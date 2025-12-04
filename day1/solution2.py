def solve():
    with open("day1/input.txt") as f:
        rotations = [line.strip() for line in f if line.strip()]

    position = 50
    zero_count = 0

    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == 'L':
            # Moving left (toward lower numbers)
            # Number of full rotations (each passes through 0 once)
            full_rotations = distance // 100
            zero_count += full_rotations

            new_position = (position - distance) % 100
            remaining = distance % 100

            # Check if we pass through 0 in the partial rotation
            # Going left from position by 'remaining' steps wraps through 0
            # if position - remaining < 0
            if remaining > 0 and position - remaining < 0:
                zero_count += 1

            position = new_position
        else:  # R
            # Moving right (toward higher numbers)
            full_rotations = distance // 100
            zero_count += full_rotations

            new_position = (position + distance) % 100
            remaining = distance % 100

            # Going right from position by 'remaining' steps wraps through 0
            # if position + remaining >= 100
            if remaining > 0 and position + remaining >= 100:
                zero_count += 1

            position = new_position

    print(zero_count)

if __name__ == "__main__":
    solve()
