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

# print(f"sums = {sums}")

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

oxygen_rating = []
co2_rating = []

for num in nums:
    if num[0] == gamma_rate[0]:
        oxygen_rating.append(num)
    else:
        co2_rating.append(num)

print(f"oxygen_rating length = {len(oxygen_rating)}")

# while oxygen_rating:
pointer = 1
sums_oxygen = {}
while len(oxygen_rating) >= 1 and pointer <= 11:
    length = len(oxygen_rating)
    for num in oxygen_rating:
        if num[pointer] == '1':
            if pointer in sums_oxygen:
                sums_oxygen[pointer] += 1
            else:
                sums_oxygen[pointer] = 1
    # if ones are more prevalent:
    if sums_oxygen[pointer] >= length//2:
        print(f"sums_oxygen[pointer] = {sums_oxygen[pointer]}")
        print(f"length//2 = {length//2}")
        for num in oxygen_rating:
            if num[pointer] == '0':
                oxygen_rating.remove(num)
    else:
        for num in oxygen_rating:
            if num[pointer] == '1':
                oxygen_rating.remove(num)

    pointer += 1

        # for x in range(1, 12):
        #     print(x)
            # if num[x] != gamma_rate[x]:
            #     oxygen_rating.remove(num)
print(pointer)
print(f"oxygen_rating = {oxygen_rating}")
# print(f"co2_rating = {co2_rating}")



# gamma =  int(gamma_rate,2)
# epsilon =  int(epsilon_rate,2)

# solution = gamma*epsilon
# print(f"solution = {solution}")