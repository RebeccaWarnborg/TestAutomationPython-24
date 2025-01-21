answer = 0
for i in range(1,101):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))

answer = 0
i = 0

while i <= 100:
    answer += i
    i += 1
print("Summan av talen 1 till 10 är: " + str(answer))


numbers = [1, -2, 3, -2, 4, -3] 
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]

print(f"total sum {sum}")