lines = open('in').readlines()

part_1 = 0
part_2 = 0

for policy, password in [line.split(': ') for line in lines]:
    freq, character = policy.split(' ')
    low, high = [int(num) for num in freq.split('-')]

    part_1 += int(low <= password.count(character) <= high)
    part_2 += int((password[low - 1] == character) != (password[high - 1] == character))

print("2a: " + str(part_1))
print("2b: " + str(part_2))
