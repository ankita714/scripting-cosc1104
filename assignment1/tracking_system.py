""" 
Name = Ankita (100941771)
Date = 11 Oct. 2024
creation of a simulated cloud storage tracking system

"""
# function for creating new user 
def create_user(user_name, storage_space, users, storage):
    
    if user_name in users:
        print("Username already exists. Please choose a different one.")
        return False
    if not user_name or storage_space <= 0:
        print("Invalid username or storage space.")
        return False
    users.append(user_name)
    storage[user_name] = {'available': storage_space, 'used': 0}
    print(f"User '{user_name}' created with {storage_space}MB storage.")
    return True

# function for deleting user 
def delete_user(user_name, users, storage):
    
    if user_name in users:
        users.remove(user_name)
        del storage[user_name]
        print(f"User '{user_name}' has been deleted.")
    else:
        print("User not found.")

# function for uploading a file 
def upload_file(user_name, file_name, file_size, storage):
    
    if user_name not in storage:
        print("User not found.")
        return False
    if storage[user_name]['available'] >= file_size:
        storage[user_name]['available'] -= file_size
        storage[user_name]['used'] += file_size
        print(f"File '{file_name}' uploaded. {file_size}MB used.")
        return True
    else:
        print("Not enough storage space.")
        return False

# function to display users and storage details  
def display_users(users, storage):
    
    print("\nCurrent Users:")
    for user in users:
        user_info = storage[user]
        print(f"Username: {user}, Available: {user_info['available']}MB, Used: {user_info['used']}MB")
    print()

def main():
    users = []
    storage = {}

    while True:
        print("\nMenu:")
        print("1. To create User")
        print("2. To delete User")
        print("3. To upload File")
        print("4. To display Users")
        print("5. Exit")

        choice = input("Enter your choice: ") # Asking for choice input 

        if choice == "1":
            user_name = input("Enter a username: ")
            space = input("Enter storage space in MB: ")
            if space.isdigit() and int(space) > 0:
                space = int(space)
                create_user(user_name, space, users, storage) # Calling creation function
            else:
                print("Invalid storage space. Must be a positive integer.")

        elif choice == "2":
            user_name = input("Enter the username to delete: ")
            delete_user(user_name, users, storage) # Calling deletion function 

        elif choice == "3":
            user_name = input("Enter the username for file upload: ")
            file_name = input("Enter the filename: ")
            file_size = input("Enter the file size in MB: ")
            if file_size.isdigit() and int(file_size) > 0:
                file_size = int(file_size)
                upload_file(user_name, file_name, file_size, storage) # Calling uploading function 
            else:
                print("Invalid file size. Must be a positive integer.")

        elif choice == "4":
            display_users(users, storage) # Call to display function 

        elif choice == "5":
            print("Exiting program.") 
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
