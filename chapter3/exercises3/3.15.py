print("Exercise 3.15")
print("\n")

cigarettes = int(input("How many cigarettes a day do you smoke? "))

print("\n")

years = int(input("How many years have you been smoking? "))

cigarettes = cigarettes * 365 * years

minutes = cigarettes * 10
days = minutes/60/24

print("\n")

print(f"You'll lose approximately {days:.0f} days because you have already smoked {cigarettes} cigarettes until now. Congrats...")