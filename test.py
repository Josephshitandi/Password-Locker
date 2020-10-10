import unittest # Importing the unittest module
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_user = User('Joseph', '123456')
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Joseph")
        self.assertEqual(self.new_user.password,"123456")
    
    def test_save_user(self):
        '''
        Test to check if the new users info is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []   
    
        
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the Credentials class behaviours.
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_credential = Credentials('Joseph','Instagram','123456')
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"Joseph")
        self.assertEqual(self.new_credential.account_name,"Instagram")
        self.assertEqual(self.new_credential.password,"123456")
    
    def test_save_credentials(self):
        '''
        Test to check if the new users info is saved into the user list
        '''
        
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)
    
    def test_delete_credentials(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Joseph","Instagram","123456") # new credential
        test_credential.save_credentials()

        self.new_credential.delete_credentials()# Deleting a credential object
        self.assertEqual(len(Credentials.credential_list),1)

   
   
   
   
        
        
        
if __name__ == '__main__':
    unittest.main()