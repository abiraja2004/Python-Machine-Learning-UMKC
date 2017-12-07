'''Create a class Student and then do the following
Create a data member to count number of students
Create a constructor to initialize name and other personal details
Create a function to calculate number of students
Create a function to display students name ,rollno and grades
Create a TransferStudent class and it should inherit the properties of Student class.
Create instances of TransferStudent and Student class and call their member functions.

    def checkCode(self, value):
        return self.pin == value
        '''
class student:
    no_of_student = 0

    def __init__(self, name,rollno,grades):
        self.name = name
        self.rollno=rollno
        self.grades=grades


    def count(self):
        self.__class__.no_of_student +=1


    def details(self):
        return "%s is student and rollno %s and has grades %s "% (self.name, self.rollno, self.grades)
#Create a TransferStudent class and it should inherit the properties of Student class.
class TransferStudent(student):
    def __init__(self,name,rollno,grades):
        student.__init__(self,name,rollno,grades)


#Create instances of TransferStudent and Student class and call their member functions.
Ali = student("Ali",23321,"B")
Ali.count()
Hasan = TransferStudent("Hasan",3232121,"C")
Hasan.count()

print(Ali.details())
print("Number of students are",Ali.__class__.no_of_student)
print(Hasan.details())
print("Number of students are",Hasan.__class__.no_of_student)


