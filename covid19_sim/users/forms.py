from  flask_login import current_user
from covid19_sim.db_models import User
from wtforms import ValidationError

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
        # self.pw_confirm = request.values.get('confirmPassword')

    def parsed(self):
        return {
            'email':self.email,
            'username':self.username,
            'password':self.password
        }
    
    
    # def validate_email(self,email):
    #     if User.query.filter_by(email=email).first():
    #         raise ValidationError('Your email has been registered already.')

    # def validate_username(self, username):
    #     if User.query.filter_by(username=username).first():
    #         raise ValidationError('Sorry, that username is taken!')

