__author__ = 'phongtrinh'

class Login() :

    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def login(self):
        print("I am in the login function")

    def click(self):
        print("I am in the click function")
