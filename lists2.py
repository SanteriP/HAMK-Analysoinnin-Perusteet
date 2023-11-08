from random import randint
thrownDiceNumbers = [randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
sum = 0

for number in thrownDiceNumbers:
    sum += number

print(*thrownDiceNumbers)
print(f"The sum is {sum}")
print(f"The highest dice roll is {max(thrownDiceNumbers)}")