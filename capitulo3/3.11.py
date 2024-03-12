print("\n")
price = float(input("Enter the price of the product: $ "))
discount = float(input("Enter the discount value in %: "))

totalDiscount = (price * discount)/100
newPrice = price - totalDiscount

print("\n")
print(f"Original price: ${price:5.2f}")
print(f"Discount: {discount:5.2f}%")
print(f"Total Discount: ${totalDiscount:5.2f}")
print(f"New Price: ${newPrice:5.2f}")
