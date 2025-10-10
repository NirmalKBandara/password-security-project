import bcrypt as bc

def hash_password(password):
    salt = bc.gensalt()
    hashed = bc.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hased):
    return bc.checkpw(password.encode('utf-8'), hased)

if __name__ == "__main__":
    password = input("Enter your password: ")

    hashed_pd = hash_password(password)
    print("\nHashed password:", hashed_pd)

    attempt = input("\nRe-enter password to verify: ")
    while(not(verify_password(attempt, hashed_pd))):
        print("❌ Password did not match!")
        attempt = input("\nRe-enter password to verify: ")
    print("✅ Password matched!")