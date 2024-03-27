import hashlib
import os

# this creates a read only file that contains a hashed password that will be used to authenticate the user

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def create_password_file(hashed_password):
    file_path = 'C:\\ProgramData\\.hidden_password.txt' 

    with open(file_path, 'w') as file:
        file.write(hashed_password)

    # this sets the file attributes to read-only and hidden
    try:
        os.system('attrib +R +H +S"{}"'.format(file_path))
        print("Password file created successfully.")
    except Exception as e:
        print("Error occurred while setting file attributes:", e)
        
def check_password(password):
    hashed_input = hash_password(password)
    file_path = 'C:\\ProgramData\\.hidden_password.txt'

    with open(file_path, 'r') as file:
        stored_password = file.read().strip()

    if hashed_input == stored_password:
        return True
    else:
        return False


# def main():
#     password = input("Enter the password to be hashed: ")
#     hashed_password = hash_password(password)
#     create_password_file(hashed_password)

# if __name__ == "__main__":
#     main()
