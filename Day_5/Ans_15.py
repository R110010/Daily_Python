#enter password till correct password is entered
correct_password = "qwerty"

while True:
    entered_password = input("Enter your password: ")
    
    if entered_password == correct_password:
        print("password entered is correct")
        break
    else:
        print("Incorrect password. Please try again.")
