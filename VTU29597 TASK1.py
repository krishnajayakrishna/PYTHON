# Get number of loaves from the user
loaves = int(input("Enter the number of day-old loaves: "))

print("Loaves Discount")

# Constants
REGULAR_PRICE_PER_LOAF = 185
DISCOUNT_RATE = 0.60

# Calculations
regular_price = REGULAR_PRICE_PER_LOAF * loaves
discount = regular_price * DISCOUNT_RATE
total_price = regular_price - discount

# Output
print("Regular Price     : Rs.", regular_price)
print("Total Discount    : Rs.", discount)
print("Amount to be paid : Rs.", total_price)
