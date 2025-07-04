#Write a function that takes two parameters: a prompt message and an error message.
#The function will prompt the user with the passed in prompt to enter an integer
#If the text entered cannot be cast to an int, display the error message.
#The function will continue to prompt the user to enter an integer until a proper integer is entered.
#The most direct way of doing this would be using a try block, which has not been covered yet. You will need to research this.
#Write supporting code to call the function, and then display the number that was entered.

# Function to prompt the user for an integer
def prompt_for_integer(prompt_message, error_message):
    while True:
        try:
            # Attempt to cast the user input to an integer
            user_input = int(input(prompt_message))
            return user_input
        except ValueError:
            # If the cast fails, display the error message and prompt again
            print(error_message)

# Supporting code to call the function and display the result
def main():
    prompt_message = "Please enter an integer: "
    error_message = "Error: That is not a valid integer. Please try again."
    
    # Call the function
    user_number = prompt_for_integer(prompt_message, error_message)
    
    # Display the entered number
    print(f"You entered the number: {user_number}")

# Start the program
if __name__ == "__main__":
    main()
