print("Exercise 4.6")
print("\n")

km = float(input("How many km do you want to travel: "))

rate = 0

if km <= 200:
   rate = 0.5
   ticket = km * rate
else:
   rate = 0.45
   ticket = km * rate

print("\n")

print(f"You are going to travel {km} km \n"
      f"The rate is ${rate:5.2f}/km \n"
      f"So, your ticket will cost ${ticket:5.2f}")