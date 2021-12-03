# now we have aim!
# down increases aim by X
# up decreases aim by X
# forward increases position by X AND increases depth by aim * X

input = open('input-day2.txt', 'r')
directions = []
for line in input:
    directions.append(line.split())

horizontal = 0
depth = 0
aim = 0

for i in range(0, len(directions)):
    if directions[i][0] == 'forward':
        horizontal = horizontal + int(directions[i][1])
        depth = depth + (aim * int(directions[i][1]))
    elif directions[i][0] == 'down':
        aim = aim + int(directions[i][1])
    elif directions[i][0] == 'up':
        aim = aim - int(directions[i][1])

print(f'Final horizontal distance: {horizontal}')
print(f'Final depth: {depth}')
print(f'Final aim: {aim}')
print(f'And if you multiply depth and horizontal distance... {horizontal * depth}')
