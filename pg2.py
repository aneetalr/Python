a=input("Enter 3 numbers seperated by ,:")
n=list(map(int,a.split(",")))
biggest=max(x for x in n)
print("Biggest number is:",biggest)
