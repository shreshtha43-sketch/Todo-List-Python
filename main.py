# 1. Add Task
# 2. View Tasks
# 3. Delete Task
# 4. Exit
Todolist=[]
print("{This is your to do list:}")
while True:
    c=int(input("Accordingly enter command:"))
    if(c==1):
        t=input("Enter task:")
        Todolist.append(t)
    elif(c==2):
        for i,task in enumerate(Todolist,start=1):
            print(f"{i}.{task}")
    elif(c==3):
        d=int(input("Which task do u want to delete(In numbers):"))
        del Todolist[d-1]
    elif(c==4):
        break
    else:
        print("No such command exist")