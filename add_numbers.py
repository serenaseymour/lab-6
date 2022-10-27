num1 = int(input("Input the first number:"))
num2 = int(input("Input the second number:"))

print("Choose an option:")
print("1. Add")
print("2. Subtract")

option = int(input())

if option == 1:
  num3 = num1 + num2
  print(f"{num1} + {num2} = {num3}")

elif option == 2:
  num3 = num1 - num2
  print(f"{num1} - {num2} = {num3}")
  
else:
  print("Error: Invalid selection")
