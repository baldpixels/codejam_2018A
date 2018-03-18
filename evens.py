import sys
import os
import math

# this function might be better off if done recursively
def find_even(number):
    presses = 0

    # list from most sig to least sig
    digits = [int(d) for d in str(number)]

    # iterate from least sig to most sig
    for n in range(0, len(digits)):
        m = len(digits) - n - 1

        if (digits[n] % 2) != 0:
        # odd case
            if n < len(digits)-1:
                if digits[n+1] < 5 or digits[n] == 9:
                # subtract case
                    sum = 0
                    for i in range(n+1, len(digits)):
                        sum += digits[i] * 10**(len(digits) - i - 1)
                        digits[i] = 8
                    powadder = 2
                    for j in range(1, m):
                        powadder += 10**j
                    presses += sum + powadder
                    digits[n] -= 1
                else:
                # add case
                    sum = 0
                    for i in range(n+1, len(digits)):
                        sum += digits[i] * 10**(len(digits) - i - 1)
                        digits[i] = 0
                    presses += 10**m - sum
                    digits[n] += 1
            else:
                presses += 1
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
        numbers[counter] = find_even(numbers[counter])
    counter += 1

# write to output file
output_file = open("output.txt", "w")

for i in range(1, len(numbers)):
    output_file.write(f'Case #{i}: ')
    output_file.write(f'{numbers[i]} ')
    output_file.write('\n')

print('\n')
print('Done! Check output.txt for results.')
