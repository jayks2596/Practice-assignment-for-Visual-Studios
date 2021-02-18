print("###################################")
print("WELCOME TO THE DBS CONSOLE")
print("###################################")

#Ask the student to enter username
student=input("Please enter your username: ")
index= student.index("\\")   

student_id=student[:index]
student_name= student[index:][1:]
#The domain and the username are displayed separately
print("Domain : ",student_id)
print("username : ",student_name)
