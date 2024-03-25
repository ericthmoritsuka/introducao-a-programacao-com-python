print("Exercise 4.3")
print("\n")

a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))

print("\n")

biggest = 0
smallest = 0

if a > b and a > c:
   biggest = a
if b > a and b > c:
   biggest = b
if c > a and c > b:
   biggest = c
if a < b and a < c:
   smallest = a
if b < a and b < c:
   smallest = b
if c < a and c < b:
   smallest = c

print(f"The smallest number is: {smallest} \n"
      f"The biggest number is: {biggest}")