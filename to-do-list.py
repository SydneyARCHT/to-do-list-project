def add_task(to_do_list):                # Ability to add tasks to the list
    task = input("What task would you like to add? ")
    to_do_list.append(task)
    print(f"Added {task} to the To-Do List")

def add_another_task(to_do_list):     # Felt like looping the same question seemed boring, 
    while True:                       # instead of retyping the menu option, felt like asking would be better. 
        response = input("Would you like to add anything else? yes/no ")
        if response == "yes":
            add_task(to_do_list)
        elif response == "no":
            break
        else:
            print("Please enter a valid response: ")

def view_tasks(to_do_list):                     # Wanted to view it as a list rather than side by side, easy to read and handle
    print("Here's the current To-Do List...")
    for task in to_do_list:
         print(task)

def task_complete(to_do_list):
        completed_todo = input("Which task has been completed?: ")
        for i, task in enumerate(to_do_list):
                if task == completed_todo:
                        to_do_list[i] += " - X"
                        print(f"{task} has been marked as finished... ")
  
def remove_task(to_do_list):      # Opposite of add_task. Prints tasks first to see what is there
    for task in to_do_list:       
         print(task)
    try:
        task = input("Which task would you like to remove? ")    
        to_do_list.remove(task)
        print(f"{task} has been removed from the To-Do list. ")  # Needs clear unstruction to see what had been removed
    except:
        print(f"{task} is not on the To-Do list, use 2. to check the current list! ")   

def remove_another_task(to_do_list):     # same thing as add_another_task but opposite. wanted to check with user
    while True:                          # if they wanted to remove something else. Looks nicer and is clearer
        response = input("Would you like to add remove else? yes/no ")
        if response == "yes":
            remove_task(to_do_list)
        elif response == "no":
            break
        else:
            print("Please enter a valid response: ")


to_do_list = []

def main(to_do_list):
    print(""" Welcome to the To-Do List App!

        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit
""")
    while True:
        response = input("Please choose from the menu above: ")
        if response == "1":
            add_task(to_do_list)
            add_another_task(to_do_list)
            print()                                   #<---- multiple print() statements. Terminal gets extremely clunky with no spaces
        elif response == "2":
            view_tasks(to_do_list)
            print()
        elif response == "3":
            task_complete(to_do_list)
            print()
        elif response == "4":
            remove_task(to_do_list)
            remove_another_task(to_do_list)
            print()
        elif response == "5":
            print(to_do_list)
            print("Take care! ")
            break
        else:
            print("Please enter a valid response... ")
            print()



main(to_do_list)



        