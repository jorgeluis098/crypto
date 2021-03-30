import fileinput

lines = []
for line in fileinput.input():
    lines.append(line)
x = 0;
for i in range(len(lines)):
    x = x + float(lines[i])
if x % 1 == 0:
    print (int(x))
else:
    print (x)