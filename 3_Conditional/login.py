default_username = 'admin'
default_password = '123456'

username = input('Username: ')
password = input('Password: ')

if username == default_username and password == default_password:
    print("Login successful")
else:
    print("Login failed")