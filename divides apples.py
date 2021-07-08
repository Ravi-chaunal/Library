n=int(input("Enter the number of apple you have:"))
mn=int(input("Enter the minimum apple you have:"))
mx=int(input("Enter the maximum apple you have:"))
print(f"you have {n} of apple")
for i in range(mn,mx+1):
    if n%i==0:
        print(f"{i} it is divisible of {n}")
    else:
        print(f"{i}it is not divisible of{n}")
 
    