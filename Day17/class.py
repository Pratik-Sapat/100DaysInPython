class User: #class name PascalCase
    def __init__(self,user_id, username): #called everytime you create new object.
        self.id = user_id
        self.username = username
        #default value.      
        self.followers = 0 
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001","Pratik")
user_2 = User("002","Rohit")
user_1.follow(user_2)

print(f"{user_1.username} = followers {user_1.followers} : following {user_1.following}")

print(f"{user_2.username} = followers {user_2.followers} : following {user_2.following}")


# print(user_1.username) #object.attribute
# print(user_2.username)
# print(user_1.followers)



#Remember.
#attributes are the things that object has. like variable.
#methods are the things that object does.
#when function attached to object then its called a method.


#how do access attribute of class.
#object.attribute
# user_2.id = "002"  #assigned value

