################# Class #################
################# Class #################

class Student:
  
  def Substraction(Self):
    a = 35
    b = 20
    return a-b
student_obj = Student()
print(student_obj.Substraction())


################# Class #################
################# Class #################

class St:
    def mult(self,a,b):
        return a*b
cl = St()
print(cl.mult(10,5))

class ss:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def mult(self):
        return self.a * self.b
    def sub(self):
        return self.a - self.b
    def div(self):
        return self.a / self.b

gg = ss(50,26)

print('Add : ',gg.add())
print('Multiplacation : ',gg.mult())
print('Substraction : ',gg.sub())
print('Division : ',gg.div())

################# Class Init #################
################# Class Init #################

class hafiz:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def Multiplacation(self):
        return self.a * self.b
ff = hafiz(52,20)
print('Multiplaction :',ff.Multiplacation())



##################  Inheritence ################
##################  Inheritence ################
##################  Inheritence ################

class Person:
    def inf(self, Name, Roll, Address, Phone):
        return Name, Roll, Address, Phone
obj = Person()
print(obj.inf('hafiz','918784','Dhaka','01646312059'))

class Student(Person):
    def stud(self):
        return

obj2 = Student()
print(obj2.inf('Rasel','8755','Patharghata','01646325059'))


class techer(Student):

    def inf(self, Name, Roll, Address, Phone, Email, ID):
        return Name, Roll, Address, Phone,Email,ID

obj3 = techer()
print(obj3.inf('Abdul Karim','8755','Patharghata','01646325059','hafizit7@gmail.com','556625'))
