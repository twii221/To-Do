class loginn:
    def login(self):
        user_name = input("Enter Your Username : ")
        password = input("Enter Your Password : ")
        for obj in self.admins:
            while obj.admin_name != user_name and obj.admin_password != password:
                print(" Sorry Username and Password Incorrect Please Re-enter for Validation ")
                user_name = input("Please Enter Your Username : ")
                password = input("Please Enter Your Password : ")
            else:
                print("Greetings,", user_name, "You are Now Logged in the System")
                break
    def upDatePassword(self,user_id,newPassword):
        if(self.__login==True):
            self.__users[user_id]=newPassword
            print("password updated")
        else:
            print("Please Login")
    
    def removeUser(self,user_id):
        if self.__login :
            del self.__users[user_id]
            print("User removed")
            self.Login=False