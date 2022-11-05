import re
pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"

pass_check = re.compile(pattern)

password = input("Enter a password containing 8 - 18 characters, an uppercase letter, a number and one special character \n")

check = re.search(pass_check, password)

if check:
    print("Valid Password")
else:
    print("Password does not meet specified critera!")




