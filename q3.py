print("###################################")
print("WELCOME TO DBS CONSOLE")
print("###################################")

list = [] 
  
#Prompt the user to enter the number of elements 
n = int(input("Input the number of elements to be stored in the list : "))
print("Input 5 elements in the list : ")  
 
for i in range(0, 5):
    ele = int(input("element:"))
  
    list.append(ele)  
      


frequency = {}
print("The frequency of all elements of the list:")
#In the for loop we check the frequency of a particular element entered by the user
for item in list:
   if (item in frequency):
      frequency[item] += 1
   else:
      frequency[item] = 1
for key, value in frequency.items():
    print("%s occurs %d times" % (key, value))
        