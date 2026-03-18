#Mirrored Right Angled Triangle
r=int(input("Enter the number of rows:"))

for nos in range(r-1,-1,-1):
    for i in range(nos):
        print(end=" ")
    noa=r-nos
    for j in range(noa):
        print(end="*")
    print()