username = input('Enter username: ')
password = input('Enter password: ')
length = len(password) # can use this expression in the formatted string
cover = '*' * length # can't use this expression in the formatted string

print(f'{username}, your password {cover} is {length} letters long.')