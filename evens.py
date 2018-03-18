import sys
import os
import re
import math

# this function might be better off if done recursively
def find_odd(number):
    presses = 0

    # list from most sig to least sig
    digits = [int(d) for d in str(number)]

    # iterate from least sig to most sig
    for i in range(len(digits)-1, -1, -1):
        if (digits[i] % 2) != 0:
        # odd case
            if i == len(digits)-1:
                if digits[i] < 6:
                    digits[i] -= 1
                else:
                    digits[i] += 1
                presses += 1
            else:
                if digits[i+1] < 6:
                    presses += (digits[i+1] + 2)*(10**(len(digits)-2-i))

                    digits[i+1] = 8

                    digits[i] -= 1
                else:
                    presses += (10 - digits[i+1])*(10**(len(digits)-2-i))

                    digits[i+1] = 0

                    digits[i] += 1

                if digits[i] > 9:
                    if i == 0:
                        digits.insert(0, 1)
                    digits[i] += 1

    #return ''.join(map(str, digits))
    return presses

# read input file
input_file = sys.argv[1]

print('EVEN DIGITS...')

with open(input_file) as f:
    file_lines = f.readlines()
f.close()

counter = 0
# digits[0] = T
numbers = [None]

for curr_line in file_lines:
    if counter == 0:
        numbers[counter] = int(curr_line)
    else:
        numbers.append(int(curr_line))
        numbers[counter] = find_odd(numbers[counter])
    counter += 1

# write to output file
output_file = open("output.txt", "w")

for i in range(1, len(numbers)):
    output_file.write(f'Case #{i}: ')
    output_file.write(f'{numbers[i]} ')
    output_file.write('\n')

print('Done.')
