class Student:
    name=str()
    rno=int()
    marks=float()

    def details(ref,section):
        ref.a=10
        ref.section=section
        ref.name=input('Enter name:')
        ref.rno=int(input('Enter roll number:'))
        ref.marks=float(input('Enter marks:'))
    @classmethod
    def subjects(ref):
        print('English\nHindi\nMaths') 
    
    def display(ref):
        print('Name:',ref.name)
        print('Roll number:',ref.rno)
        print('Marks:',ref.marks)
        print('Section:',ref.section)

s1=Student()
s1.details("A")
Student.subjects()
s1.display()            