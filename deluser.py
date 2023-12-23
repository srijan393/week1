def delete_user(username, file_path="passwd.txt"):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    found = False
    with open(file_path, 'w') as file:
        for line in lines:
            if not line.startswith(username + ":"):
                file.write(line)
            else:
                found = True

    if found:
        print("User Deleted.")
    else:
        print("User not found.")

if __name__ == "__main__":
    username = input("Enter username: ")
    delete_user(username)
