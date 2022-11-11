
class User:
    def __init__(self,first_name, last_name, age, email):
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
        self.email= email
        self.gold_cardvalue= 0
        self.is_rewards_member= False    
    def display_info(self):
        print(f'{self.first_name}\n{self.last_name}\n{self.age}\n{self.email}\n{self.gold_cardvalue}\n{self.is_rewards_member}')
    def enroll(self):
        self.is_rewards_member = True
        self.gold_cardvalue = 200
    def spend_points(self,amount):
        self.gold_cardvalue-=amount
        
new_user = User("Zacc","Buk",20,"Zacfa@gmail.com")
new_user2 = User("Will","Fa",18,"Willfa@gmail.com")
new_user3 = User("Richardson","Faze",21,"Richardsonfa@gmail.com")
new_user.display_info()
print('------------------')
new_user3.enroll()
new_user3.display_info()    #This User is a member because their card_value = the defualt  200 to be a member
# points spent line 26
print('------------------')
new_user.enroll()
new_user.spend_points(50)
new_user.display_info()   # This User has 80 less than 200 there for they are not a member and have false displayed 
print('------------------')
new_user2.enroll()
new_user2.spend_points(80)
new_user2.display_info()  # This User has 80 less than 200 there for they are not a member and have false displayed 