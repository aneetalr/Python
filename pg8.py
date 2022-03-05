from datetime import date
today=date.today()
year=today.year
future=int(input("Enter a future year:"))
leap=[x for x in range(year,future+1) if (x%400==0) or (x%100!=0) and (x%4==0)]
print("leap years are :",leap)
