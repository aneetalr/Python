n=input("Enter the naems seperated by ,:")
name=n.split(",")
count=[c for c in name if c.lower().startswith("a")]
print(len(count))
