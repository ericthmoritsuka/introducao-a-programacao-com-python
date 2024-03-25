print("Exercise 4.4")
print("\n")

salary = float(input("Enter the salary: $ "))

raisePercentage = 0

if salary > 1250:
   raisePercentage = 10
if salary <= 1250:
   raisePercentage = 15

raiseValue = salary*raisePercentage/100

print("\n")

print(f"The salary was ${salary:5.2f} \n"
      f"There was a {raisePercentage}% raise \n"
      f"{raisePercentage}% of ${salary:5.2f} = ${raiseValue:5.2f} \n"
      f"So, the new salary is ${(salary + raiseValue):5.2f}.")
