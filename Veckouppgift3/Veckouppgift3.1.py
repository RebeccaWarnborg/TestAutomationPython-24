for i in range (10):
    if i == 5:
        print("")
    else:
        print(i)
        i = 1 + 1

counter = 0
for i in range (6):
    counter += i
    print (counter)

x = 0
y = 1 
while y < 10:
    if y % 2 == 0:
        x -= y
    else: 
        x += y * y 
    y += 1

message = "its_time_to_get_coding"
print(message[4:8])

for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y + 1:
            s += "#"
        else:
            s += "."
    print(s)