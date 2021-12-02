input = open('input.txt', 'r').read().splitlines()

x = y = 0

for line in input:
    op, amount = line.split()
    amount = int(amount)
    if op == 'forward':
        x += amount
    elif op == 'down':
        y += amount
    elif op == 'up':
        y -= amount
print(x*y)

x = y = aim = 0

for line in input:
    op, amount = line.split()
    amount = int(amount)
    if op == 'forward':
        x += amount
        y += amount*aim
    elif op == 'down':
        aim += amount
    elif op == 'up':
        aim -= amount
print(x*y)
