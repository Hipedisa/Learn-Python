# To do list
import sys

list = []

print("============================ To Do List ============================")

def printList():
    for i in range(len(list)):
        print(str(i + 1) + ". " + list[i])

while True:
    task = input("Enter a task to put in your list. Type \"done\" if you're finished.\n").strip()
    
    if task.lower() == "done":
        printList()
        break
    elif task == "":
        print("Please enter a valid task!")
        continue
    else:
        list.append(task)

if not list:
    print("No tasks found!")
    sys.exit()

while list:
    
    try:
        removedTask = int(input("Select which task you're done with to remove it. (1, 2, 3, etc..) "))
        
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    if removedTask not in range(1, len(list) + 1):
        print("Please enter a valid number!")
        continue

    del list[removedTask - 1]

    if list:
        printList()
    else:
        print("All tasks completed!")
    
input("Press enter to continue...")