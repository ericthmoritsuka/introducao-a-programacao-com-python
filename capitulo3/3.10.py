salary = float(input("Enter the salary: "))
porcentage = float(input("Enter the raise (%): "))

raiseValue = salary * porcentage / 100
newSalary = salary + raiseValue

print("\n")
print(f"Salary: ${salary:5.2f}")
print(f"Raise: {porcentage}% => ${raiseValue}")
print(f"New Salary: ${newSalary:5.2f}")
