def change_password(username, current_password, new_password, file_path="passwd.txt"):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    found = False
    with open(file_path, 'w') as file:
        for line in lines:
            if line.startswith(username + ":"):
                _, _, stored_password = line.split(":")
                if current_password == stored_password.strip():
                    line = f"{username}:{real_name}:{new_password}\n"
                    found = True
                else:
                    print("Current password is invalid.")
            file.write(line)

    if found:
        print("Password changed.")
    else:
        print("User not found.")

if __name__ == "__main__":
    username = input("User:             ")
    real_name = input("Real Name:        ")
    current_password = input("Current Password: ")
    new_password = input("New Password:     ")
    confirm_password = input("Confirm:          ")

    if new_password != confirm_password:
        print("Passwords do not match.")
    else:
        change_password(username, current_password, new_password)
