# Welcome message
print("Welcome to the Multiplication Table Generator!")

# Infinite loop to repeatedly ask for input until a valid number is provided
while True:
    # Get user input (converted to an integer)
    number = int(input("Enter a positive number to generate its multiplication table: "))
    
    # If-else condition to check if the input is valid
    if number > 0:
        # If the number is positive, print the multiplication table
        print(f"Multiplication Table for {number}:")
        
        # Use a for loop to generate the table for numbers 1 through 10
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
        
        # Exit the loop once the table is generated
        break
    else:
        # If the number is zero or negative, display an error message
        print("Invalid input! Please enter a positive number.")
        # The loop continues, asking the user to input a valid number
