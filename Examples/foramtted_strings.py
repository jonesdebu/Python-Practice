#formatted strings
#python 3 version
name = "Johnny"
age = 55
print(f'hi {name}. You are {age} years old.')

print()

#python 2 versions
print('hi {}. You are {} years old.'.format(name, age))

print()
#or
print('hi {1}. You are {0} years old.'.format(name, age))

#where name = 0 and age = 1
#so it will print the variables backwards

print('hi {new_name}. You are {age} years old.'.format(new_name = 'Sally', age=100))

