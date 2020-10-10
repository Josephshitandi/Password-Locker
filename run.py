import pyperclip
from user import User
from credentials import Credentials
import random #import random variable generator
import string  #import string constants


def create_user(user_name,password):
    '''
    Function to create new user
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save new user account
    '''
    User.save_user
    
def verify_user(user_name,password):
    '''
    Function that veryfies the existing user
    
    '''
    check_user = Credentials.check_user(user_name,password)
    return check_user


def create_credential(user_name,account_name,password):
    '''
    Function that creates new creadential
    '''
    new_credential = Credentials(user_name,account_name,password)
    return new_credential

def check_existing_account(account_name):
    '''
    Function that checks if ctredential exists
    '''
    return Credentials.find_by_account_name(account_name)

def generate_password():
    '''
    Function that generates password automatically
    '''
    password_generated = Credentials.generate_password()
    return password_generated

def save_credentials(credential):
    '''
    Function that saves new credential
    '''
    Credentials.save_credentials(credential)
    
def delete_credential(credential):
    '''
    Function that deletes a credential
    '''
    Credentials.delete_credentials(credential)
    
def find_credential(account_name):
    '''
    Function that credential by account_name and returns credential
    '''
    return Credentials.find_by_account_name(account_name)

def display_credential(credentials):
    '''
    Function that displays saved credentials
    '''
    return Credentials.display_credentials()

def main():
    # print('')
    print('Hello! Welcome to password Locker')
    while True:
        print("--"*50)
        print('\n')
        
        print('Use these short codes: \n ca - Create an Account \n lg - Login \n ex - Exit')
        print('\n')
        short_code = input().lower() 
        if short_code == 'ex':
            break 
        
        elif short_code == 'ca':
            print("-"*20)
            print('\n')
            print('Create a new account:')
            print('\n')

            
            user_name = input('Enter your User name - ')
            password = input('Enter your password - ')
            save_user(create_user(user_name, password))
            print(" ")
            print(
                f'New Account Created for: {user_name} using password: {password}')
            print('\n')

        elif short_code == 'lg':
            print("--"*50)
            print('\n')
            print('Enter your account details to login:')
            print('\n')

            username = input('Enter your user name - ')
            password = str(input('Enter your password - '))
            user_exists = verify_user(username,password)
            if user_exists == username:
                print('\n')
                print(f'Welcome {username}. Please select a short code to continue.')
                print(' ')

                while True:
                    print("-"*30)
                    print('Our short codes: \n cc-Create a Credential \n sc-Show Credentials \n fc- Find a Credential  \n ex-Exit')
                    print('\n')
                    short_code = input('Enter a choice: ').lower()
                    print("-"*10)


                    if short_code == 'ex':
                        print(" ")
                        print(f'Thank you for using Password Lock. Goodbye {username}')
                        break

                    elif short_code == 'cc':
                        print('\n')
                        print('Enter your new credentials:')
                        print('\n')  
                        account_name = input('Enter your account name - ')

                        while True:
                            print('\n')
                            print("-"*20)
                            print('Please select an option for creating a password: \n ep - enter your password \n gp - generate a password \n ex - exit')
                            choice = input('Enter an option: ').lower()
                            print("-"*10)
                            
                            













if __name__ == '__main__':
	main()