import re

def check_password(password):
    points = 0
    arr = []

    if len(password) < 8:
        return "Password is short!"
    else:
        points += 1

    if not(re.search(r"[a-z]", password)):
        arr.append("Password should contain at least one lower case character")    
    else:
        points += 1

    if not(re.search(r"[A-Z]", password)):
        arr.append("Password should contain at least one upper case character")
    else:
        points += 1

    if not(re.search(r"[\d]", password)):
        arr.append("Password should contain at least one digit")
    else:
        points += 1

    if not(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        arr.append("Password should contain at least one special character")
    else:
        points += 1

    if points == 5:
        remarks = "Very strong"
    elif points == 4:
        remarks = "Strong"
    elif points == 2:
        remarks = "Medium"
    else:
        remarks = "Weak" 

    for wd in arr:
        print(wd)

    return remarks     

if __name__ == "__main__":
    password = input("Enter Your Password to Check: ")
    result =  check_password(password)
    print("Strengt:", result)
