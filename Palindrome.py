number=int(input("enter the integer:"))
temp = number 
reversed_number = 0   # because we start from 1
while number !=0:
    x = number %10    # x is remainder
    number=number//10 # one more way number //=10
    reversed_number = reversed_number * 10 + x 
print(reversed_number)
if(reversed_number==temp):
 print("True")
else:
    print("false")
