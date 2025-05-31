class Student:
    total_marks=600

    def __init__(self,name,Id,Marks,):
        self.Id=Id
        self.name=name
        self.Marks=Marks
    def display(self):
        print("Name :",self.name)  
        print("Id :",self.Id)
        print("Marks :",self.Marks) 
        print("Percentage : ",(self.Marks/self.total_marks)*100) 
        with open("st.txt","a") as f1:
            f1.write(f"Name: {self.name}\n")
            f1.write(f"Id: {self.Id}\n")
            f1.write(f"Marks: {self.Marks}\n")
            f1.write(f"Percentage: {(self.Marks / self.total_marks) * 100}%\n")
            f1.write("\n") 

        
students=[]
num=int(input("Enter number of Students you enter Data : "))
for i in range(num):
 name=input("Enter Name : ")
 id=int(input("Enter Id : "))
 Marks=int(input("Enter Marks : ")) 
 st=Student(name,id,Marks)
 students.append(st)
print("Details of Students") 
for st in students:

  st.display()

  
