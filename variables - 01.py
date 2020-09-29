#exercise1
#x=2
#y=4
#name="daniel"
#print(name * y)
#doron=3
#liran=5
#ilay=6
#print (doron, liran, ilay)
#total_apple=14
#print(total_apple)

#exercise2
#x1=str(input("enter name:"))
#x2=int(input("enter number:"))
#print(x1*x2)

#exercise3
#x1=float(input("enter hours:"))
#x2=float(input("rate per hour:"))
#print("payment:",end=(""))
#print(x1*x2)

#exercise4 - both students
#student1c=float(input("enter student1 computer science score:"))
#student1m=float(input("enter student1 math score:"))
#student2c=float(input("enter student2 computer science score:"))
#student2m=float(input("enter student2 math score:"))
#print("your students average score is:",end=(" "))
#print((student1c+student1m+student2c+student2m)/4)

#exercise4 - each student
#student1c=float(input("enter student1 computer science score:"))
#student1m=float(input("enter student1 math score:"))
#student2c=float(input("enter student2 computer science score:"))
#student2m=float(input("enter student2 math score:"))
#print("your student2 average score is:",end=(" "))
#print((student2c+student2m)/2)
#print("your student1 average score is:",end=(" "))
#print((student1c+student1m)/2)

#exercise5
#busrent=float(input("enter bus payment:"))
#park=float(input("enter park payment:"))
#students=int(input("how many students?"))
#print((busrent+park)/students)

#exercise6
#pants=int(input("how many pants:"))
#shirts=int(input("how many shirts:"))
#pricep=float(input("how much for each pant:"))
#prices=float(input("how much for each shirt:"))
#print("total price:",end=" ")
#print((pants*pricep+shirts*prices)*0.8)

#exercise7
#popsicle=0.8
#chocolate_ice_cream=2.4
#popsicleamount=int(input("how many popsicles:"))
#icecreamamount=int(input("how many ice creams:"))
#print("total price:",end=" ")
#print((icecreamamount*chocolate_ice_cream+popsicleamount*popsicle)*1.17)

#exercise8
#hour = int(input("Starting time (hours): "))
#mins = int(input("Starting time (minutes): "))
#dura = int(input("Event duration (minutes): "))
#H = (dura+mins)//60+hour
#M = (dura+mins)%60
#if H > 24:
#    H = H-24
#print(H,":",M)