num_trib=int(input("Enter the number of tribonacci numbers you want:"))
print(num_trib)

num1=1
print(num1)
num2=1
print(num2)
num3=2
print(num3)

for num in range(num_trib-3):
    num4=num1+num2+num3
    print(num4)
    num1=num2
    num2=num3
    num3=num4