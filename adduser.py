def add_user(username, real_name, password, file_path="passwd.txt"):
    with open(file_path, 'a') as file:
        file.write(f"{username}:{real_name}:{password}\n")
    print("User Created.")

if __name__ == "__main__":
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = input("Enter password: ")
    add_user(username, real_name, password)
