nums = [int(x) for x in open('in').readlines()]

for x, num1 in enumerate(nums):
    for y, num2 in enumerate(nums[x + 1:]):
        if num1 + num2 == 2020:
            print("1a: " + str(num1 * num2))

        for z, num3 in enumerate(nums[y:]):
            if num1 + num2 + num3 == 2020:
                print("1b: " + str(num1 * num2 * num3))
