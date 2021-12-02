# considering three-part sums increasing

input = open('input-day1.txt', 'r')
data = []
for line in input:
    data.append(int(line.strip()))

increases = 0

for i in range(0, len(data)-3):
    triad = sum(data[i:i+3])
    next = sum(data[i+1:i+4])
    if next > triad:
        increases += 1

print(f'Final result: {increases}')

# for line in data:
