def user_name():
    email = input("Enter your email address: ")
    at_position = email.find('@')

    if at_position != -1:
        username = email[:at_position]
        return username
    else:
        print('Invalid address')

username = user_name()
print('Your Username is', username)

