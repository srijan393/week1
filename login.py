def login(username, password, file_path="passwd.txt"):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith(username + ":"):
                _, _, stored_password = line.split(":")
                stored_password = stored_password.strip()
                if password == stored_password:
                    print("Access granted.")
                    return

    print("Access denied.")

if __name__ == "__main__":
    username = input("User:     ")
    password = input("Password: ")
    login(username, password)
