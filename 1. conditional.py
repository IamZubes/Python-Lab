def password_maker(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    elif not any(char.isdigit() for char in password):
        return "Password must contain at least one number."
    elif not any(char.isalpha() for char in password):
        return "Password must contain at least one letter."
    else:
        return "Password is valid!"

password = input("Enter your password: ")
result = password_maker(password)
print(result)