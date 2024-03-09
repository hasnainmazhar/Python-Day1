# 1. Print Statement and Comments
favorite_quote = "The only limit to our realization of tomorrow will be our doubts of today."
print(favorite_quote)
# Comment: This quote inspires me because it emphasizes the importance of overcoming doubts and believing in the future.

# 2. Escape Sequences
print("Your Name\nYour Age")

# 3. Type Casting
user_age_str = input("Enter your age: ")
user_age_int = int(user_age_str)
print("Your age as an integer:", user_age_int)

# 4. Operators
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("Area of the rectangle:", area)

# 5. Print Formatting
name = "John"
age = 25
print(f"My name is {name}, I am {age} years old. Welcome!")

# 6. Escape Sequences and Comments
print("Proper\tformatting\tis\timportant\tin\tprogramming.")
# Comment: Proper formatting improves code readability and makes it easier to maintain.

# 7. Type Casting and Operators
input_number = float(input("Enter a number: "))
result = int(input_number) * 2
print("Result after type casting and multiplication:", result)

# 8. Multiple Statements
for i in range(1, 4):
    print(5 * i)

# 9. Comments and Type Casting
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
average = (num1 + num2) / 2
# Comment: Calculating the average of two numbers.
print("Average:", average)

# 10. Operators and Escape Sequences
message_with_quote = 'This is a message with a single quote (\') using escape sequences.'
concatenated_message = message_with_quote + " Concatenated with another string."
print(concatenated_message)

# 11. Type Casting and Print Formatting
input_float = float(input("Enter a number: "))
converted_int = int(input_float)
print(f"The integer value of {input_float} is {converted_int}.")

# 12. Operator Challenge
num1_challenge = float(input("Enter the first number: "))
num2_challenge = float(input("Enter the second number: "))
result_challenge = round(num1_challenge / num2_challenge, 2)
print("Result of division rounded to two decimal places:", result_challenge)

# 13. Escape Sequences and Comments
print("This line ends with a backslash.\\")  # Comment: The backslash is used to escape the newline character.

# 14. Operator Challenge - II
input_number_challenge = float(input("Enter a number: "))
square = input_number_challenge ** 2
square_root = input_number_challenge ** 0.5
print(f"Square: {square}, Square Root: {square_root}")

# 15. Type Casting and Comments
user_weight_str = input("Enter your weight: ")
user_weight_float = float(user_weight_str)
print(f"Your weight is {user_weight_float} kilograms.")
# Comment: Converting user's weight from string to float for accurate calculations.
