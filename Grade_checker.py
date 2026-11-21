# Ask a user to input a numeric grade (0-100)
grade = int(input("Please enter a numeric grade (0-100): "))

# Determine the letter grade based on the numeric grade
if grade >= 90:
    letter_grade = "A"
elif grade >= 80:
    letter_grade = "B"
elif grade >= 70:
    letter_grade = "C"
elif grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Your grade is {letter_grade}.")

# Final message using conditional expression
final_message = "Congratulations! You passed!" if letter_grade in ["A", "B", "C"] else "Sorry, you failed. Better luck next time!"

print(final_message)