class Credentials:
    '''
    Class to create  account credentials, generate new passwords and save user information
    '''
    
    credentials_list =[]
    
    def __init__(self,user_name,account_name,password):
        '''
        Method to define the properties for each user object.
        '''
        self.user_name = user_name
        self.account_name = account_name
        self.password = password