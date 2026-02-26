base=int(input("Enter the base number:"))
n= int(input("Enter the power(n):"))    

result=1

for i in range(n):
    result*=base
print("Result:", result )