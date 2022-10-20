#! Python3

# Project 3 - E-mail SLicer
# A program which slices e-mail adresses

# Get user E-mail address
user_email = input("Please enter your E-mail: ").strip()

# Slice out user name
user_name = user_email[:user_email.index("@")]

# Slice domain name
user_domain = user_email[user_email.index("@") + 1:]

# Format message
message = f"Your username is {user_name} abd your domain name is {user_domain}"

# Display output message
print(message)
