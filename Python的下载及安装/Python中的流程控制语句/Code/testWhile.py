while True:
    print("Please input your username:")
    userName = input()
    print("Please input your password:")
    password = input()
    if userName == "admin" and password == "123456":
        print("Welcome!",userName)
        break
    else:
        print("Please try entering your username and password again!")
    
