# Write a function that accepts a number as an argument and returns a string
# containing that number along with its "ordinal indicator".
# E.g. passing in 1 would return "1st", 2 would return "2nd", 3 would return "3rd",
# 4 would return "4th", etc.
#
# Make sure your function works for every number between 1 and 20.
# If you're feeling ambitious, see if you can get it working for numbers beyond that.

# For numbers beween 1 and 110

# Works up to 110

def ordinal(number):

    if number % 10 == 1 and number != 11:
        print(str(number) + "st")
    elif number % 10 == 2 and number != 12:
        print(str(number) + "nd")
    elif number % 10 == 3 and number != 13:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")


ordinal(1)
ordinal(2)
ordinal(3)
ordinal(4)
ordinal(5)
ordinal(6)
ordinal(7)
ordinal(8)
ordinal(9)
ordinal(10)
ordinal(11)
ordinal(12)
ordinal(13)
ordinal(14)
ordinal(15)
ordinal(16)
ordinal(17)
ordinal(18)
ordinal(19)
ordinal(20)
ordinal(21)
ordinal(22)
ordinal(23)
ordinal(24)
ordinal(103)
ordinal(111)
ordinal(131)
ordinal(142)
ordinal(153)
ordinal(201)
