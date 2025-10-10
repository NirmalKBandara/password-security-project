import bcrypt as bc
import json as js
import os

DATA_FILE = "vault.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return js.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        js.dump(data, file, indent = 4)

def add_password(account, password):
    data = load_data()
    salt = bc.gensalt()
    hashed  = bc.hashpw(password.encode('utf-8'), salt)
    data[account] = hashed.decode('utf-8')
    save_data(data)
    print(f"\nPassword for '{account}' added successfully.")

def verify_password(account, password):
    data = load_data()
    if account not in data:
        print("\nAccount not found.")
        return
    
    hashed = data[account].encode('utf-8')
    if bc.checkpw(password.encode('utf-8'), hashed):
        print("\nPassword verified successfully!")
    else:
        print("\nPassword did not match!")

def main():
    print("\nSimple Password Managar...")
    print("\n1. Add new password")
    print("2. Verify existing password")
    print("3. Exit")

    choice = input("\nEnter your choice(number): ")

    if choice == "1":
        print("\nEnter account name | ex: example@fake.xyz")
        account = input(">>> ")
        print("Enter password")
        password = input(">>> ")
        add_password(account, password)

    elif choice == "2":
        print("\nEnter account name:")
        account = input(">>> ")
        print("Enter password:")
        password = input(">>> ")
        verify_password(account, password)

    elif choice == "3":
        print("\nFarewell...")
        exit()

    else:
        print("\nInvalid choice!")


if __name__ == "__main__":
    while True:
        main()
