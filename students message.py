names= []
mAssign = []
grades = []
num = int(input("how many students:"))
if num < 0:
    print("invalid input")
namesLength = num
    #and create a list for the students
#ask the user for a list of names of the students
while len(names) < namesLength:
    name= input("name -")
    names.append(name)
#names = ["ephraim", "esther", "andre"]
#ask the user for a list of missing assignments
    mAss = int(input("missed assignments-"))
    mAssign.append(mAss)
#ask the user for a list of current grades
    cGrades = int(input("grade? "))
    grades.append(cGrades)
#using a loop
for message in range (num):
    new = int(grades[message]+(2*(mAssign[message])))
    #print out the message
    print("HI, {} , this is a reminder that you have {}\
assignments left to submit befor you can graduate,\
your current grade is, {} and can increase to {} if you\
submit all assignments befor the due date\n\n".format(names[message],mAssign[message],grades[message],new))

