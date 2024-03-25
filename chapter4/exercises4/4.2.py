print("Exercise 4.2")
print("\n")

speed = float(input("What was your speed (in km/h)? "))

print("\n")

if speed > 80:
   speedOver = speed - 80
   fine = speedOver * 5
   print("You were over the speed limit. \n"
         f"Your speed was {speed} km/h \n"
         f"You were {speedOver} km/h above the limit. \n"
         f"Here is your fine: R$ {fine} \n"
         "Congratulations...")
else:
   print("Congratulations! You respect the law.")