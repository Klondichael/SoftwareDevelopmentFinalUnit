# 9-3
class User:

    def __init__(self, first_name, last_name, username, email, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        
        self.login_attempts = login_attempts # 9-5
    
    def describe_user(self):
        print(self.username)
        print(f"\t{self.first_name} {self.last_name}")
        print(f"\t{self.email}")
    
    def greet_user(self):
        print(f"Hello {self.first_name}!")
    
michael = User("Michael", "Hickey", "Klondichael", "michael.j.hickey@outlook.com")
liam = User("Liam", "Mackey", "MrMacAttack3374", "liam.mackey08@gmail.com")
ava = User("Ava", "Xagaras", "earth _isflat623", "axagaras@hotmail.com")

michael.describe_user()
michael.greet_user()
liam.describe_user()
liam.greet_user()
ava.describe_user()
ava.greet_user()