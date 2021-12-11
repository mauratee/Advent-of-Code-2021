import unittest

def parse_input(input_file):
    lines = []
    with open(input_file) as f:
        for line in f:
            line = line.strip('\n')
            lines.append(line)
    f.close()
    return lines

# lines = parse_input("day10_input.txt")
example = parse_input("example_input.txt")

# print(lines[0:10])
# print(example[0:10])

def calculate_score(character):
    if character == ')':
        return 3
    if character == ']':
        return 57
    if character == '}':
        return 1197
    if character == '>':
        return 25137

def find_corrupted_lines(list_lines):

    openers = {"(": ")", "{": "}", "[": "]", "<": ">"}
    closers = {")": "(", "}": "{", "]": "[", ">": "<"}

    bracket_stack = []

    total_score = 0

    for line in list_lines:
        for char in line:
            if char in openers:
                bracket_stack.append(char)
                # print(bracket_stack)
            else:
                if char in closers:
                    print(f"we're in closers!")
                    if not bracket_stack:
                        print(f"char = {char}")
                        score = calculate_score(char)
                        print(f"score = {score}")
                        total_score += score
                        print(f"total_score = {total_score}")
                        continue
                    else:
                        if bracket_stack[-1] == closers[char]:
                            bracket_stack.pop()
                print(f"we're in else, bracket stack = {bracket_stack}")

    return total_score
            


print(find_corrupted_lines(example))

# Class Test(unittest.TestCase):

#     def test_zer_decimal(self):
#         actual = isAmount("100")
#         expected = True
#         self.assertEqual(actual, expected)

#     def test_empty_string(self):
#         actual = isAmount("")
#         expected = False
#         self.assertEqual(actual, expected)

#     def test_one_decimal(self):
#         actual = isAmount("1.1")
#         expected = False
#         self.assertEqual(actual, expected)

#     def test_alpha(self):
#         actual = isAmount("Hello. I")
#         expected = False
#         self.assertEqual(actual, expected)

#     def test_negative(self):
#         actual = isAmount("-10")
#         expected = True
#         self.assertEqual(actual, expected)
    
#     def test_special_char(self):
#         actual = isAmount("%^^^%.($")
#         expected = False
#         self.assertEqual(actual, expected)
    
#     def test_two_decimal(self):
#         actual = isAmount("100.20")
#         expected = True
#         self.assertEqual(actual, expected)

#     def test_three_decimal(self):
#         actual = isAmount("100.200")
#         expected = False
#         self.assertEqual(actual, expected)

#     def test_lots_decimals(self):
#         actual = isAmount("100.2000000000000")
#         expected = False
#         self.assertEqual(actual, expected)


# unittest.main(verbosity=2)
