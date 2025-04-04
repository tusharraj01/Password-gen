import random
import string

# Function to generate a password
def generate_password(length):
    # Define the characters to use in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters from the list
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Main program to get user input
if __name__ == "__main__":
    try:
        # Ask user for the password length
        length = int(input("Enter the desired password length: "))
        
        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid integer for the password length.")

    # Prevent the window from closing immediately
    input("Press Enter to exit...")
