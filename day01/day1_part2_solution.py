
depths = []
num_increases = 0

with open("day1_input.txt") as f:
    for line in f:
        # current = line.readline()
        line = line.strip('\n')
        depths.append(int(line))

f.close()
# print(depths[0:10])

for x in range(len(depths)-3):
    A = (depths[x] + depths[x+1] + depths[x+2])
    B = (depths[x+1] + depths[x+2] + depths[x+3])
    if B > A:
        num_increases += 1

print(num_increases)