# TodoLogic.py
# 6411271 LYNN THIT NYI NYI

import ToolBox as Tb
List = []

def func1():
    task = input("Enter task name: ")

    while True:
        try:
            priority = int(input("Enter priority level: ")) #Room for improvement
            
            #restricting users from entering integers that are not 1,2,3 for priority for easier data handling
            while priority < 1 or priority > 3:
                print("Priority level must be an integer 1,2, or 3")
                priority = int(input("Please re-enter priority level (1-3): "))
            
            
        except ValueError:
            print("Priority level must be an integer 1,2, or 3")
            continue
        else:
            break

    #the prioritites entered by users can only be integers 1,2,3
    
    status1 = 'I' #all added tasks are originally incomplete
    
    temp1 = []
    temp1.append(task)
    temp1.append(priority)
    temp1.append(status1)
    
    List.append(temp1)
    
    print(f'New task added at {Tb.getTime()}')


def func2():
    while True:
        try:
            i = int(input("Enter task index: "))
        except ValueError:
            print("Please enter an integer")
            continue
        else:
            break
    
    if i >= 0 and i <= len(List)-1: #will not accept negative values for better convenience
        List[i][2] = 'C'
        #print(List)#testing
        print(f"{List[i][0]} completed at {Tb.getTime()}")
        
    elif i > len(List)-1 or i < 0:
        
        print("Task not found!")


def func3():
    from operator import itemgetter
    
    tempList3 = [] #temp list so that original list stays original
    
    for i in range(len(List)):
        if List[i][2] == 'I':
            tempList3.append(List[i])

    if len(tempList3)>0: #if there is at least one incomplete tasks
        
        tempList3.sort(reverse=True,key=itemgetter(1)) #sort according to descending priority
        
        print('Priority \tTask(s)') #display
        for i in range (len(tempList3)):
            print(f"{Tb.priorityName(tempList3[i][1])}\t\t{tempList3[i][0]}")
            
    else: #if there are no incomplete tasks at all
        
        print("No incomplete tasks.")

    #print(List) #testing

def func4():
    while True:
        try:
            priority4 = int(input("Enter priority level: "))

            #This block of code can be used to restrict users from entering integer values that are not 1,2,or 3
            #If this code isn't used, priority levels will be 'N/A' for integer values that are not 1,2,or 3
            #And there will not be any tasks that has the priority level 'N/A'
            #because we restricted users from entering integer values that are not 1,2,or 3 in function 1 for priority
            '''
            while priority < 1 or priority > 3:
                print("Priority level must be an integer 1,2, or 3")
                priority = int(input("Please re-enter priority level (1-3): "))
            '''
                
        except ValueError: #if input is not an integer
            print("Please enter an integer value.") #print message and loop
            
        else:
            break
    
    tempList4 = []
    
    for i in range(len(List)):
        if List[i][2] == 'I' and List[i][1] == priority4:
            tempList4.append(List[i])

    if len(tempList4)>0:
        print('Priority \tTask(s)') #recheck spacing
        for i in range (len(tempList4)):
            print(f"{Tb.priorityName(tempList4[i][1])}\t\t{tempList4[i][0]}")
    else:
        print(f"No incomplete tasks for {Tb.priorityName(priority4)} priority level.")

def func5():
    print('Summary Report')
    numI = 0 #number of incomplete tasks
    numC = 0 #number of completed tasks

    HighI = 0 #number of high priority incomplete tasks
    MedI = 0 #number of medium priority incomplete tasks
    LowI = 0 #number of low priority incomplete tasks

    HighC = 0 #number of high priority completed tasks
    MedC = 0 #number of medium priority completed tasks
    LowC  = 0 #number of low priority completed tasks

    #priorities entered by users can ONLY BE INTEGERS 1,2,3
    #Therefore, 3 if-elif statements for 1,2 and 3 is enough
    #And, no else statements will be required
    
    for i in range(len(List)):
        if List[i][2] == 'I': #if incomplete
            numI += 1
            if List[i][1] == 1:
                LowI += 1
            elif List[i][1] == 2:
                MedI += 1
            elif List[i][1] == 3:
                HighI += 1 
        elif List[i][2] == 'C': #if complete
            numC += 1
            if List[i][1] == 1:
                LowC += 1
            elif List[i][1] == 2:
                MedC += 1
            elif List[i][1] == 3:
                HighC += 1 

    print(f"No. of incomplete tasks is {numI} (High={HighI}, Medium={MedI}, Low={LowI})")
    print(f"No. of complete tasks is {numC} (High={HighC}, Medium={MedC}, Low={LowC})")


def func6():
    while True:
        try:
            i6 = int(input("Enter task index: "))
        except ValueError:
            print("Please enter an integer")
            continue
        else:
            break
        
            
    if i6 >=0 and i6 <= len(List)-1: #will not accept negative values for better convenience
        print(f"{List[i6][0]} removed!")
        List.remove(List[i6])
    elif i6 > len(List)-1 or i6 < 0:
        print("Task not found!")
    #print(List) #testing


def func7():
    count7 = 0
    for i in range(len(List)):
        if List[i][2] == 'I':
            count7 += 1
    if count7 >0:
        for i in range(len(List)):
            if List[i][2] == 'I':
                List[i][2] = 'C'
                print(f"{List[i][0]} completed at {Tb.getTime()}")
    else:
        print("No incomplete tasks")


def menu():
    print("\nTODO List Menu Driven")
    print("PERSONAL TASK REMINDER")
    print("---- ---- ---- ---- ---- ---- ----")
    print("1. Create a new task")
    print("2. Mark completes for a specific task")
    print("3. Show incomplete tasks, sort by priority")
    print("4. Show incomplete tasks for a specific priority")
    print("5. Show summary report")
    print("6. Remove a specific task")
    print("7. Mark completes for every tasks you have")

    
def menuuserInput():
    while True:
        try:
            uInput = int(input("Enter option (1-7, 0 to exit): "))
            while uInput < 0 or uInput > 7:
                uInput = int(input("Please enter a valid option (1-7, 0 to exit): "))
        except ValueError:
            print("Please enter an integer!\n")
            continue
        else:
            break
    return uInput

def run():
    menu()
    UInput = menuuserInput()
    print("---- ---- ---- ---- ---- ---- ----")
    while UInput != 0:
        if UInput == 1:
            func1()
        if UInput == 2:
            func2()
        if UInput == 3:
            func3()
        if UInput == 4:
            func4()
        if UInput == 5:
            func5()
        if UInput == 6:
            func6()
        if UInput == 7:
            func7()
        menu()
        UInput = menuuserInput()
        print("---- ---- ---- ---- ---- ---- ----")
    print('End of program. See you next time!')
    
