import hashlib
import os

# this creates a read only file

# Function to hash the password
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Function to create a hidden read-only file with hashed password
def create_password_file(hashed_password):
    # Specify the file path
    file_path = 'C:\\ProgramData\\.hidden_password.txt'  # You can change this path as needed

    # Write the hashed password to the file
    with open(file_path, 'w') as file:
        file.write(hashed_password)

    # Set the file attributes to read-only and hidden
    try:
        os.system('attrib +R +H "{}"'.format(file_path))
        print("Password file created successfully.")
    except Exception as e:
        print("Error occurred while setting file attributes:", e)

# Main function
def main():
    password = input("Enter the password to be hashed: ")
    hashed_password = hash_password(password)
    create_password_file(hashed_password)

if __name__ == "__main__":
    main()
