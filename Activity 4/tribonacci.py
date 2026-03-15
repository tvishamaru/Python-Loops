num_fib=int(input("Enter the number of fibonacci numbers you want:"))
print(num_fib)

num1=1
print(num1)
num2=1
print(num2)
num3=2
print(num3)

for num in range(num_fib-3):
    num4=num1+num2+num3
    print(num4)
    num1=num2
    num2=num3
    num3=num4