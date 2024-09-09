dict1={101:['Krishna','Management',10000]}
print(dict1)

def addemployee(dict1):
    name=input("Enter employee name: ")
    eid=int(input("Enter employee id: "))
    dept=input("Enter department: ")
    salary=int(input("Enter Salary: "))
    items={eid:['name','dept',salary]}
    dict1.update(items)
   
def updaterec(dict1):
    eid=int(input("enter employee id: "))
    for id in dict1.keys():
        if(eid!=id):
            print("employee not found")
        else:
            ch=int(input("what do you want to update"))
            if(ch==1):
                name1=input("Enter new name of employee: ")
                dict1[eid][0]=name1
            elif(ch==2):
                dept1=input("Enter new dept of employee: ")
                dict1[eid][1]=dept1
            elif(ch==3):
                salary1=int(input("Enter new salary of employee: "))
                dict1[eid][2]=salary1
            else:
                          print("Invalid Choice")
    print(dict1)
   
   
   
def searchemp(dict1):
    eid=int(input("enter employee id: "))
    for id in dict1.keys():
            if(eid!=id):
                print("employee not found")
            else:
                print(dict1.get(eid))
addemployee(dict1)
updaterec(dict1)          
searchemp(dict1)
##def deptreport(dept):
##    count=0
##    dept=input("enter department you want the number of: ")
##    for dept1 in dict1.values():
 ##       if(dept==dept1):
  ##          count+=1
   ## print(count)
##deptreport(dict1
