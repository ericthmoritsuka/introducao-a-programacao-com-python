distance = float(input("Enter the amount of km traveled: "))

print("\n")

days = int(input("Enter the amount of days the car was rented for: "))

print("\n")

priceDays = days * 60
priceDistance = distance * 0.15

total = priceDays + priceDistance

print(f'You rented the car for {days} days.\n'
      f'Each day costs $60. The total is ${priceDays:5.2f}. \n'
      f'You traveled for {distance}km \n'
      f'Each km costs $0.15. The total is ${priceDistance:5.2f}. \n'
      f'The grand total is ${total:5.2f}')
