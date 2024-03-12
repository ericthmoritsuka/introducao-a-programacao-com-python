print("\n")
distance = float(input("Enter the distance in KM: "))
averageSpeed = float(input("Enter the assumed average speed in KM/H: "))

tripDurationHours = distance/averageSpeed
hours = tripDurationHours // 1
minutes = (tripDurationHours - hours) * 60

if tripDurationHours >= 1:
   print("\n")
   print(f"You will travel {distance}km")
   print(f"You plan to drive at {averageSpeed}km/h")
   print(f"You will reach your destination in: {hours:5.2f} hour(s) and {minutes:5.0f} minute(s)")
else:
   print("tripDurationHours < 1")
   print("\n")
   print(f"You will travel {distance}km")
   print(f"You plan to drive at {averageSpeed}km/h")
   print(f"You will reach your destination in: {hours:5.2f} hour(s) and {minutes:5.0f} minute(s)")