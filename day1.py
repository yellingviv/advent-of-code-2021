# counting how many times the depth increases via the input

data = open('input-day1.txt', 'r')

counter = 0
prev = 0
increases = 0

for line in data:
    if counter > 0:
        if line > prev:
            increases += 1
            prev = line
        else:
            prev = line
    elif counter == 0:
        prev = line
    counter += 1
