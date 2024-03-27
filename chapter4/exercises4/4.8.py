print("Exercise 4.8")
print("\n")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

choice = input("Which operation do you want to perform?\n"
                 "Enter 1 for ADDITION (+)\n"
                 "Enter 2 for SUBTRACTION (-)\n"
                 "Enter 3 for MULTIPLICATION (*)\n"
                 "Enter 4 for DIVISION (/)\n")

result = 0
operator = ''

if choice == '1':
   operator = '+'
   result = a + b
elif choice == '2' :
   operator = '-'
   result = a - b
elif choice == '3' :
   operator = '*'
   result = a * b
elif choice == '4' :
   operator = '/'
   result = a / b

print("\n")

print(f"{a} {operator} {b} = {result:5.2f}")