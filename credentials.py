from user import User
import random #import random variable generator
import string  #import string constants


class Credentials:
    '''
    Class to create  account credentials, generate new passwords and save user information
    '''
    
    credential_list = []
    
    def __init__(self,user_name,account_name,password):
        '''
        Method to define the properties for each user object.
        '''
        self.user_name = user_name
        self.account_name = account_name
        self.password = password
    
    
    def save_credentials(self):
        '''
        A method that saves new user object
        '''
        Credentials.credential_list.append(self)    
        
    def delete_credentials(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credentials.credential_list.remove(self)        
        
    @classmethod
    def check_user(cls,user_name,password):
        '''
        Method that checks if the name and password entered exist in the users_list
        '''
        current_user = ''
        for user in User.user_list:
        	if (user.user_name == user_name and user.password == password):
        		current_user = user.user_name
        return current_user

 

    def generate_password(self,size=10, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate a secure 10 character password for a user.
        '''
        password_gen=''.join(random.choice(char) for _ in range(size))
        return password_gen

	# @classmethod
	# def display_credentials(cls,username):
	# 	'''
	# 	Method to display the list of credentials saved.
	# 	'''
	# 	user_credentials_list = []
	# 	for credential in cls.credentials_list:
	# 		if credential.username == username:
	# 			user_credentials_list.append(credential)
	# 	return user_credentials_list



	# @classmethod
	# def find_by_site_name(cls, site_name):
	# 	'''
	# 	Method that takes in a site_name and returns a credential that matches that site_name.
	# 	'''
	# 	for credential in cls.credentials_list:
	# 		if credential.site_name == site_name:
	# 			return credential
	# 	return False

	# @classmethod
	# def copy_credential(cls,site_name):
	# 	'''
	# 	Method that copies a credential to the clipboard.
	# 	'''
	# 	try:
	# 		find_credential = Credential.find_by_site_name(site_name)
	# 		print(f'Your Password for {site_name} has been copied. You can paste it anywhere now.')
	# 		return pyperclip.copy(find_credential.password)
	# 		time.sleep(10)
	# 		pyperclip.copy("")
	# 		print("Password destroyed from clipboard")
			
	# 	except 	AttributeError: 
	# 		return "Invalid site name" 

        
        