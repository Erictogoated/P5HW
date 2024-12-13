# Eric corbett
# 11/23/2024
# P5HW 
# This is a math quiz program that asks the user to guess the result of random addition or subtraction problems.

import random

# Function to perform addition and check user input
def add_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    print(f"Add the following numbers: {num1} + {num2}")
    user_answer = int(input("What is the result? "))
    
    if user_answer == correct_answer:
        print("Correct! Great job!")
    else:
        print(f"Oops! The correct answer is {correct_answer}.")

# Function to perform subtraction and check user input
def subtract_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, num1)  
    correct_answer = num1 - num2
    print(f"Subtract the following numbers: {num1} - {num2}")
    user_answer = int(input("What is the result? "))
    
    if user_answer == correct_answer:
        print("Correct! Well done!")
    else:
        print(f"Oops! The correct answer is {correct_answer}.")

# Main menu function to display options
def display_menu():
    print("\nMenu:")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Exit")
    choice = input("Choose an option (1, 2, or 3): ")
    return choice

# Main program logic
def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            add_numbers()  
        elif choice == '2':
            subtract_numbers()  
        elif choice == '3':
            print("Thank you for playing! Goodbye!")
            break  
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
