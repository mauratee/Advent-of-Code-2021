# from bitstring import BitArray

nums = []

with open("day3_input.txt") as f:
    for line in f:
        line = line.strip('\n')
        nums.append(line)

f.close()
print(nums[0:10])

sums = {}

for num in nums:
    for x in range(12):
        if num[x] == '1':
            if x in sums:
                sums[x] += 1
            else:
                sums[x] = 1

print(f"sums = {sums}")

gamma_rate = []
epsilon_rate = []

for x in range(12):
    num = sums[x]
    if num < 500:
        gamma_rate.append('0')
        epsilon_rate.append('1')
    else:
        gamma_rate.append('1')
        epsilon_rate.append('0')

gamma_rate = ("").join(gamma_rate)
epsilon_rate = ("").join(epsilon_rate)


print(f"gamma_rate = {gamma_rate}")
print(f"epsilon_rate = {epsilon_rate}")

gamma =  int(gamma_rate,2)
epsilon =  int(epsilon_rate,2)
print(gamma)

# print(f"horizontal = {horizontal}")
# print(f"vertical = {vertical}")

solution = gamma*epsilon
print(f"solution = {solution}")