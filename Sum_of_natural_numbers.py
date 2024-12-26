print("Natural numbers addition calculator")

n = int(input("\nEnter the natural number "))
sum = 0
i = 0

while i < n+1:
    sum += i
    i += 1

print("Result = ", sum)