import unittest

def parse_input(input_file):
    lines = []
    with open(input_file) as f:
        for line in f:
            line = line.strip('\n')
            lines.append(line)
    f.close()
    return lines

lines = parse_input("day10_input.txt")
# print(lines)
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
        # print(f"line = {line}")
        for char in line:
            if char in openers:
                bracket_stack.append(char)
                # print(bracket_stack)
            else:
                if char in closers:
                    # print(f"we're in closers!")
                    if not bracket_stack:
                        # print(f"char = {char}")
                        score = calculate_score(char)
                        # print(f"score = {score}")
                        total_score += score
                        # print(f"total_score = {total_score}")
                        continue
                    
                    if bracket_stack[-1] == closers[char]:
                        bracket_stack.pop()
                    else:
                        if bracket_stack[-1] != closers[char]:
                            score = calculate_score(char)
                            # print(f"score = {score}")
                            total_score += score
                            # print(f"total_score = {total_score}")
                            break
                # print(f"we're in else, bracket stack = {bracket_stack}")
        bracket_stack = []

    return total_score
            
# # <<<<<<< PART 1 >>>>>>>
print(f"PART 1:")
print("answer is ", find_corrupted_lines(lines))

def find_incomplete_lines(list_lines):

    openers = {"(": ")", "{": "}", "[": "]", "<": ">"}
    closers = {")": "(", "}": "{", "]": "[", ">": "<"}

    bracket_stack = []
    to_be_completed = []
    completed_reversed = []

    for line in list_lines:
        # print(f"line = {line}")
        for char in line:
            if char in openers:
                bracket_stack.append(char)
                # print(bracket_stack)
            else:
                if char in closers:
                    # print(f"we're in closers!")
                    if bracket_stack[-1] == closers[char]:
                        bracket_stack.pop()
                    else:
                        bracket_stack = []
                        break
                # print(f"we're in else, bracket stack = {bracket_stack}")
        bracket_stack.reverse()
        # print((bracket_stack))
        to_be_completed.append(("").join(bracket_stack))
        bracket_stack = []

    # for string in to_be_completed:
    #     string = string.reverse()
    #     completed_reversed.append(string)

    return to_be_completed

def calculate_score(list_to_complete):
    openers = {"(": ")", "{": "}", "[": "]", "<": ">"}
    scores = []

    for item in list_to_complete:
        score = 0
        for char in item:
            character = openers[char]
            # print(f"score = {score}")
            score = (score*5)
            # print(f"score = {score}")
            if character == ')':
                score += 1
            if character == ']':
                score += 2
            if character == '}':
                score += 3
            if character == '>':
                score += 4
            # print(f"score = {score}")
        scores.append(score)
    
    return scores

print(f"PART 2:")
# print(find_incomplete_lines(lines))
scores = (calculate_score(find_incomplete_lines(lines)))
final_Scores = []
for score in scores:
    if score != 0:
        final_Scores.append(score)
# print(final_Scores)
answer = sorted(final_Scores)
index = len(answer)//2
# print(index)
print("answer is", answer[index])
