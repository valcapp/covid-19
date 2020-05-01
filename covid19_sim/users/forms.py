from  flask_login import current_user
from covid19_sim.db_models import User

class LoginForm():
    def __init__(self, request):
        self.email = request.values.get('userEmail')
        self.password = request.values.get('userPassword')
    
    def parsed(self):
        return {
            'email':self.email,
            'password':self.password
        }

class RegistrationForm():
    def __init__(self,request):
        self.email = request.values.get('userEmail')
        self.username = request.values.get('userName')
        self.password = request.values.get('userPassword')
        print('Registration Form: ',self.parsed()) 

    def parsed(self):
        return {
            'email':self.email,
            'username':self.username,
            'password':self.password
        }
    
