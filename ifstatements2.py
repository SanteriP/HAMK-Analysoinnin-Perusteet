number1 = 7
number2 = 5
number3 = 4

if number1 == number2 and number1 == number3:
    print("All numbers are equal")

if number1 == number2 or number2 == number3:
    print("Either number1 and number2 or number2 and number3 are equal.")

if number1 > number2 and number1 > number3:
    print("number1 is greater than number2 and number3")

if number1 > number2:
    print("number1 is greater than number2")

elif number2 > number3:
    print("number2 is greater than number3")

if number1 == number2:
    print("number1 and number2 are equal")

elif number1 == number3:
    print("number1 and number3 are equal.")