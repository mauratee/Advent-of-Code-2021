import sys

print(sys.argv)

all_nums = []
drawn_nums_int = []

with open("day4_input.txt") as f:
    for line in f:
        line = line.strip('\n')
        all_nums.append(line)

f.close()
print(all_nums[0])
drawn_string = all_nums[0]

drawn_nums = drawn_string.split(",")
for num in drawn_nums:
    num = int(num)
    drawn_nums_int.append(num)
    
print(drawn_nums)
print(drawn_nums_int)