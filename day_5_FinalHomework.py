#Homework
#Create a Simple Student Management System:

# -One student must enter their name and surname.
# -A student who enter name and surname correctly should write "welcome" on the screen with print. 
# The Student has the right to enter his/her name and surname incorrectly 3 times. For more than
# 3 inccorect entiries, the system shuts down and the message "Please try again later" 
# should be printed on the screen.
# -5 courses should be created and those courses should be kept in a list.
# All of these lessons be taken from the user.
# -This student can take minimum of 3 and maximum of 5 lessons.
# -This student can not take less than 3 courses.
# -Otherwise the message 'You failed in class' should be returned to student by using return statement.
# -The student must choose one of these courses and take an exam. Add the grades from this 
# course to a dictionary and keep the student's grades in this dictionary as midterm, 
# final and project grades.
# *Example: {'midterm':38, 'final':68, 'project':89}
#  -Percentages for grades
#  -Midterm Exam: %30
#  -Final Exam: %50
#  -Project: %20
# -Determine a course passing grade according to the grades received.
#  -For notes,
#             - If the grade is>90, the student should get AA
#             - If 70<grade<90 BB
#             - If 50<grade<70 CC
#             - If 30<grade<50 DD
#             - If x<30 FF, let FF take
#     - if student has received FF, he/she should print his/her failure on screen. 

 
 
grades =  {'Midterm':20,'Final':20,'Project':80}

print("Welcome, enter correct name and surname combo to continue")
count = 0
while count < 3:

    _name = str(input("Please enter your user name: "))
    _surname = str(input("Please enter your surname: "))
    count+=1
    if _name=='Ongun' and _surname=='Bosnak':
        print('Welcome Ongun BOSNAK')
        break 
        
    else:
        print("Please try again later!")

courses=["Mat","Tr","Eng","Fr","Bilişim"]
newlist = []
i=0
x=0
j=input("How many lessons do you want to take:")
if int(j)<  3:
   print ("You failed..You have to take class more than 2 ")
   exit(0)
print(f'{courses} you may choose these lessons')
while x < int(j):
   a = input("Enter your lessons :")
   if a in courses:
      newlist.append(a)
      x+=1
      
   else : 
    print("this lesson not available")

      
print(newlist)
exam_course = input("Please enter the name which you want to learn grade? ")      
grades["Midterm"] = int(input("Please enter your Midterm grade :"))
grades["Final"] = int(input("Please enter your Final grade :"))
grades["Project"] = int(input("Please enter your Project grade :"))
FinalGrade = 0.3*grades["Midterm"] + 0.5*grades["Final"] + 0.2*grades["Project"]

if FinalGrade > 90:
    print("Your grade is AA")
elif FinalGrade > 70:
    print("Your grade is BB")
elif FinalGrade > 50:
     print("Your grade is CC")
elif FinalGrade > 30:
     print("Your grade is DD")
elif FinalGrade < 30:
     print("Your grade is FF")