# counting how many times the depth increases via the input

data = open('input-day1.txt', 'r')

counter = 0
prev = 0
increases = 0
decreases = 0

for line in data:
    if counter > 0:
        if line > prev:
            increases += 1
            prev = line
        elif line < prev:
            prev = line
            decreases += 1
    elif counter == 0:
        prev = line
    counter += 1

print(f'Total counters: {counter}')
print(f'Final decrease count: {decreases}')
print(f'Final increase count: {increases}')
