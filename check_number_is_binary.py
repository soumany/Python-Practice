number =int(input("Enter the integer:"))
while number !=0:
    number=number//10
    remainder = number%10
    if (remainder!=0 and remainder!=1):
      print("False")
      break
    if (number==0):
      print("True")
