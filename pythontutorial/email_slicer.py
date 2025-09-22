mail = input("Enter your email: ")

index = mail.index("@")

username = mail[:index]
domain = mail[index+1:]

print(f"Your username is {username} and domain is {domain}")