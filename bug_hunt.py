count = 1
total = 0

# BUG: The while statement was missing a colon.
# Added : at the end of the condition.
# BUG: The condition count < 5 excluded 5 from the sum.
# Changed it to count <= 5 to include numbers 1 through 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The program tried to concatenate a string and an integer.
# Converted total to a string using str(total).
print("Sum of 1 to 5 is: " + str(total))