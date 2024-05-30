# ** to add power (2 ** 3 = 8)
# round (float number) returns rounded-off float number (round(2.66666) = 3)
# round can also be used to round up a number up to some decimal numbers (round(2.66666, 2) = 2.66)
# but the issue with this approach is when you have only one digit after decimal.
# and you want to print decimal up to 2 places. For this, you use the format function which returns a String.
# "{:.2f}".format(6.3) = 6.30
# // divides two numbers and returns integer (8 // 3 = 2)

print("Welcome to the tip calculator!")
bill = float(input("What was your total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
bill += bill*tip/100
people = int(input("How many people to split the bill? "))
split = "{:.2f}".format(round(bill/people, 2))
print("Each person should pay: $" + split)
