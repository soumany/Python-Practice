line=input("Enter the Numbers on one line:")
print("Line:",line)
tokens=line.split()
print("Token:",tokens)
total=0
for s in tokens:
  total=total+float(s)
print("Total:",total)