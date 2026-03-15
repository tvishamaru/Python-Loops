# Ask how many Fibonacci numbers does the user want
# Print that many Fibonacci numbers starting with 1 & 1
# Next number in Fibonacci number series is the sum of the previous 2 numbers

num_fib=int(input("Enter the number of fibonacci numbers you want:"))
print(num_fib)

num1=1
print(num1)
num2=1
print(num2)

for num in range(num_fib-2):
    num3=num1+num2
    print(num3)
    num2=num1
    num1=num3