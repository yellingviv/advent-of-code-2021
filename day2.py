# calculate the movement forward, up, down, etc then multiply the final position

input = open('input-day2.txt', 'r')
directions = []
for line in input:
    directions.append(line.split())

horizontal = 0
depth = 0

for i in range(0, len(directions)):
    if directions[i][0] == 'forward':
        horizontal = horizontal + int(directions[i][1])
    elif directions[i][0] == 'down':
        depth = depth + int(directions[i][1])
    elif directions[i][0] == 'up':
        depth = depth - int(directions[i][1])

print(f'Final horizontal distance: {horizontal}')
print(f'Final depth: {depth}')
print(f'And if you multiply them... {horizontal * depth}')
