# ** to add power (2 ** 3 = 8)
# round (float number) returns rounded-off float number (round(2.66666) = 3)
# round can also be used to round up a number up to some decimal numbers (round(2.66666, 2) = 2.66)
# // divides two numbers and returns integer (8 // 3 = 2)

print("Welcome to the tip calculator!")
bill = float(input("What was your total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
bill += bill*tip/100
people = int(input("How many people to split the bill? "))
split = round(bill/people, 2)
print(f"Each person should pay: ${split}")
