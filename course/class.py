import sys
from io import StringIO

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        grade = None
        average = sum(self.scores)/len(self.scores)
        if 90 <= average <= 100:
            grade = "O"
        elif 80 <= average < 90:
            grade = "E"
        elif 70 <= average < 80:
            grade = "A"
        elif 55 <= average < 70:
            grade = "P"
        elif 40 <= average < 55:
            grade = "D"  
        elif average < 40:
            grade = "T"  
        
        return grade

sys.stdin = StringIO("""
Heraldo Memelli 8135627
100 80  
""".strip())

line = sys.stdin.readline().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, sys.stdin.readline().split()) )
s = Student(firstName, lastName, idNum, scores)
# s.printPerson()
# print("Grade:", s.calculate())

print(isinstance(s, Student))   #对象实例
print(isinstance(s, Person))    #True
print(type(s) is Student)       #类
print(type(s) is Person)        #False