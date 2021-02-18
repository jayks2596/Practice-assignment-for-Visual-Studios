import datetime 
#Prompting the user to enter employee details
ename= input("Enter name of employee:")
enum= input("Enter employee number:")

#Prompting the user to enter week ending date
date= print("Enter week ending date:")
year = int(input('Enter a year:'))
month = int(input('Enter a month:'))
day = int(input('Enter a date:'))
date1 = datetime.date(year, month, day)
print("year-month-day:",date1)

#Prompting the user to enter the number of hrs worked, standard tax rate and ovrtime tax rate
hrs=float(input("Enter number of hours worked:"))
hr_rate=float(input("Enter hourly rate:"))
ovrtime=float(input("Enter overtime rate:"))
st_rate=float(input("Enter standard tax rate:"))
ot_rate=float(input("Enter overtime tax rate:"))

#Calculations
ovrtime_rate=(hr_rate*1.5)
th_pay=37.50*hr_rate
after_ded_1=((th_pay*20)/100)
ovrtime_1=hrs-37.50
th_pay1=ovrtime_1*hr_rate*ovrtime
after_ded_2=th_pay1-((th_pay1*50)/100)
total_pay=th_pay+th_pay1
print("total",total_pay)
total_ded=after_ded_1+after_ded_2
print("Total deduction",total_ded)
net_pay=th_pay+th_pay1-total_ded
print("Net pay",net_pay)

#Output
print("\n                                             P A Y S L I P")  
print("WEEK ENDING", date1)  
print("Employee :", ename)
print("Employee Number: " ,enum)  
print("                                    Earnings                     Deductions      ")                 
print("                                    hrs     Rate   Total                             ")
print("hrs (normal)                      37.50     "+   str(hr_rate)+"    "+str(th_pay)+          "      Tax @ "+str(st_rate)+"%  "+   str(after_ded_1))
print("hrs (ovrtime)                    "+str(ovrtime_1)+"      "+str(ovrtime_rate)+"   "+ str(ovrtime_1*ovrtime_rate)+   "      Tax @ "+str(ot_rate)+"% "+ str(after_ded_2))

print("Total pay:",total_pay)
print("Total deductions:",total_ded)   
print("Net pay:",net_pay)
