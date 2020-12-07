import sys

sys.setrecursionlimit(1000000)
descs = open('in').read().splitlines()

tree = {}
for desc in descs:
    outer_bag = desc.split("bags contain ")[0].strip()

    for inner_bag in desc.split('bags contain ')[1].split(", "):
        inner_bag_color = " ".join(inner_bag.split(" ")[1:3])
        if inner_bag_color in tree:
            tree[inner_bag_color].append(outer_bag)
        else:
            tree[inner_bag_color] = [outer_bag]


def get_containing_bags(bags):
    containing = []
    for bag in bags:
        if bag in tree:
            containing += tree[bag]

    return containing


def part1(bags):
    if len(get_containing_bags(bags)) == 0:
        return bags
    else:
        return bags + part1(get_containing_bags(bags))

print("7a: ", len(set((part1(["shiny gold"])))) - 1)

tree = {}
for desc in descs:
    outer_bag = desc.split("bags contain ")[0].strip()

    for inner_bag in desc.split('bags contain ')[1].split(", "):
        inner_bag_color = " ".join(inner_bag.split(" ")[0:3])
        if outer_bag in tree:
            tree[outer_bag].append(inner_bag_color)
        else:
            tree[outer_bag] = [inner_bag_color]


def get_bags_contained_by(bags):
    containing = []
    for bag in bags:
        if bag in tree:
            for contained in tree[bag]:
                if contained != "no other bags.":
                    containing += int(contained.split(" ")[0]) * [" ".join(contained.split(" ")[1:])]

    return containing


def part2(bags):
    if len(get_bags_contained_by(bags)) == 0:
        return bags
    return bags + part2(get_bags_contained_by(bags))

print("7b:", len(part2(["shiny gold"])) - 1)