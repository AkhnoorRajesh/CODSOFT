import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password by randomly choosing characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user to specify the desired length of the password
length = int(input("Enter the desired length of the password: "))

# Generate the password
password = generate_password(length)

# Display the generated password
print("Generated Password:", password)
