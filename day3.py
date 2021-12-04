# find the most common 1/0 for each digit of binary lists
# concatenate to make the gamma rate
# then flip (where 1, put 0, etc) for the other rate
# convert both from binary, multiply to get power consumption

binary_input = open('input-day3.txt', 'r')
num_len = len(binary_input.readline()) - 1

nums = {}
final_num = []

for i in range(0, num_len):
    nums[i] = {0: 0, 1: 0}

for line in binary_input:
    bin_num = line.split()[0]
    for i in range(0, num_len):
        if bin_num[i] == '0':
            nums[i][0] += 1
        elif bin_num[i] == '1':
            nums[i][1] += 1

for i in range(0, num_len):
    if nums[i][0] > nums[i][1]:
        final_num.append('0')
    else:
        final_num.append('1')

gamma = ''.join(final_num)
epsilon = ''

for i in range(0, len(gamma)):
    if gamma[i] == '0':
        epsilon = epsilon + '1'
    else:
        epsilon = epsilon + '0'

power = int(gamma, 2) * int(epsilon, 2)
print(power)
