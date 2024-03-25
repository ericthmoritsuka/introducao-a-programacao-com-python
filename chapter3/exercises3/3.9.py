print("Exercise 3.9")
print("\n")

days = int(input("Enter the days: "))
hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

daysConverted = days*24*60*60
hoursConverted = hours*60*60
minutesConverted = minutes*60
total = daysConverted + hoursConverted + minutesConverted + seconds

print("\n")
print(f"Converting {days} days => {daysConverted} seconds")
print(f"Converting {hours} hours => {hoursConverted} seconds")
print(f"Converting {minutes} minutes => {minutesConverted} seconds")

print(f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds => {total} seconds")