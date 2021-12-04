# o2 is most common number in bit position if tied, use 1
# co2 is least common number in bit position but 0 if tied

binary_input = open('input-day3.txt', 'r')
og_nums = []
for line in binary_input:
    og_nums.append(line.strip())
cols = len(og_nums[0])

def get_col_val(col_num, nums):
    # get the more common and less common values for a column
    # return 1 if tied -- co2 nums wants opposite of what it gets anyways

    zero = 0
    one = 0
    for line in nums:
        if line[col_num] == '0':
            zero += 1
        elif line[col_num] == '1':
            one += 1
    if int(zero) > int(one):
        return '0'
    elif int(zero) < int(one):
        return '1'
    elif zero == one:
        return '1'


def get_reduced_nums(col, nums, req):

    o2_nums = []
    co2_nums = []
    key = get_col_val(col, nums)
    for i in range(0, len(nums)):
        if nums[i][col] == key:
            o2_nums.append(nums[i])
        else:
            co2_nums.append(nums[i])
    if req == 'o2':
        return o2_nums
    else:
        return co2_nums


def pass_the_nums():

    o2_working = og_nums
    co2_working = og_nums
    for i in range(0, cols):
        if len(o2_working) > 1:
            o2_working = get_reduced_nums(i, o2_working, 'o2')
        if len(co2_working) > 1:
            co2_working = get_reduced_nums(i, co2_working, 'co2')

    return o2_working, co2_working

ohtwo_bin, seeoh_bin = pass_the_nums()
ohtwo = int(ohtwo_bin[0], 2)
seeoh = int(seeoh_bin[0], 2)
life_support = ohtwo * seeoh

print(life_support)
