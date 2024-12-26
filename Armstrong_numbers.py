print("Armstrong number finder")

num = int(input("\nEnter a number "))
inte = num
sum1 = 0
n = 0

while inte > 0:
    n = inte%10
    sum1 += n**3
    inte //= 10

if num == sum1:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
