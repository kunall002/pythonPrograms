# Example program demonstrating the use of if statements, while loops, for

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Iterate over the list using a for loop
for number in numbers:
# If the number is even, skip to the next iteration using the continue
    if number % 2 == 0:
        continue
 # If the number is 7, stop iterating using the break statement
    if number == 7:
        break
# If the number is not 7 and is odd, print it
        print(number)
 # If the number is less than 4, do nothing using the pass statement
    if number < 4:
        pass
# Define a variable
i = 0
# Create a while loop that continues until i is equal to 5
while i < 5:
 # If i is even, skip to the next iteration using the continue statement
    if i % 2 == 0:
        i += 1
        continue
 # If i is equal to 3, stop iterating using the break statement
    if i == 3:
        break
 # If i is odd, print it
    print(i)
 # If i is less than 2, do nothing using the pass statement
    if i < 2:
        pass
 # Increment i
    i += 1
# Define a string
word = "python"
# Iterate over the characters in the string using a for loop
for char in word:
 # If the character is 't', skip to the next iteration using the continue

    if char == 't':
        continue
# If the character is 'h', stop iterating using the break statement
    if char == 'h':
        break
# If the character is not 'h' or 't', print it
print(char)
# If the character is 'y', do nothing using the pass statement
if char == 'y':
    pass
# End of program