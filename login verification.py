user_name=input("Enter your username ? \n ")
password=int(input("Enter your password ? \n "))
if user_name=="admin" and password==1234:
    print("Welcome to the admin panel")
    check=input("do you have a two step verification ? \n ")
    if check=="yes":
        admin_code=input("Enter your admin code ? \n ")
        if admin_code=="0000":
            print("you are logged in successfully")        
        else:
            print("invaild!")
    else:
        print("successfully logged in (no two step verification)!")        
else:
    print("invaild user name or password")              