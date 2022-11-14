import datetime

user = input("New user? ")
if user.lower() == "yes":
    print("sign in")
    first_name = input("first name: ")
    if len(first_name) < 2:
        print("name not valid")
    elif len(first_name) > 50:
        print("name not valid")
    surname = input("surname: ")
    if len(surname) < 2:
        print("name not valid")
    elif len(surname) > 50:
        print("name not valid")
    email_count = 0
    email_limit = 4
    while email_count < email_limit:
        email_count += 1
        email_address = input("email address: ")
        email_address_confirmation = input("confirm email: ")
        if email_address != email_address_confirmation:
            print("email incorrect")
        else:
            break
    else:
        print("number of trials exceeded")

# determine the password length and confirmation
    password_count = 0
    password_limit = 4
    while password_count < password_limit:
        password_count += 1
        password = input("password: ")
        if len(password) < 8:
            print("password too short")
        elif len(password) > 50:
            print("invalid password")
        else:
            print("good")
        password_confirmation = input("confirm password: ")
        if password != password_confirmation:
            print("incorrect")
        else:
            break
    else:
        print("entry exeeded")
        exit()
#to determine the age validity of user
    year_birth = input("year of birth: ")
    month_birth = input("month of birth: ")
    day_birth = input("day of birth")

    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    current_day = datetime.date.today().day
    try:
        age =current_year - int(year_birth)
    except:
        age = -1
    if age > 18:
        print("proceed")
    elif age < 0:
        print("invalid")
    else:
        print("not eligible")
        exit()
    country = input("country of origin ")
    address = input("physical address: ")
elif user.lower() == "no":
    print("log in")
    user_name = input("user name: ")
    user_password = input("password: ")
else:
    print("invalid")
credit = 0