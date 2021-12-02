directions = []

with open("day2_input.txt") as f:
    for line in f:
        # current = line.readline()
        line = line.strip('\n')
        line = line.split(" ")
        directions.append([line[0], int(line[1])])

f.close()
# print(directions[0:10])

horizontal = 0
vertical = 0
aim = 0

for direction in directions:
    if direction[0] == 'forward':
        horizontal += direction[1]
        vertical += (direction[1] * aim)
    elif direction[0] == 'down':
        aim += direction[1]
    else:
        aim -= direction[1]

print(f"horizontal = {horizontal}")
print(f"vertical = {vertical}")

solution = horizontal*vertical
print(f"solution = {solution}")