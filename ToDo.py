print("Welcome to task manager.")
task=[]
num=int(input("How many tasks do you want to do today? "))
for i in range(0, num):
    todo=input("Enter your task: ")
    task.append(todo)
print("Today's tasks are",task)

while True:
    oper=int(input("Enter \n1-Add a new task\n2-Update an existing task\n3-Delete an existing task\n4-View all the tasks\n5-Exit program\nSo what do you want to do? "))
    if oper==1:
        add=input("What task to add? ").lower()
        task.append(add)
    elif oper==2:
        update=input("Which task to update? ").lower()
        if update in task:
            upd=input("Enter new task: ").lower()
            task[task.index(update)]=upd
    elif oper==3:
        delt = input("Which task to delete: ").lower()
        if delt in task:
            del task[task.index(delt)]
    elif oper==4:
        print(task)
    else:
        break
print("Thank you for using this to-do list.")