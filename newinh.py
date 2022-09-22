class company:
    def input(self):
        self.name=input("Enter company name:")
        self.location=input("Enter company")
    
    
    def show(self):
        print(self.name)
        print(self.location)
        
class employee(company):
    def input1(self):
        self.ename=input("Enter employee name:")
        self.eID=int(input("Enter employee ID"))
        
    def show1(self):
        print(self.ename) 
        print(self.eID)
s1=employee()
s1.input()
s1.input1()
s1.show()
s1.show1()