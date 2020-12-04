trees = [c.strip() for c in open('in').readlines()]


def trees_hit(trees, slope):
    pos = (0, 0)
    hit = 0

    while pos[1] < len(trees):
        hit += int(trees[pos[1]][pos[0] % len(trees[pos[1]])] == "#")

        pos = (pos[0] + slope[0], pos[1] + slope[1])

    return hit


print("3a: ", str(trees_hit(trees, (3, 1))))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (5, 2)]

part2 = 1
for slope in slopes:
    part2 *= trees_hit(trees, slope)

print("3b: ", str(part2))

