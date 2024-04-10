
import sys #imports the "sys" module or System-specific paramaeters and functions

#This module provides access to some variables used or maintained by the interpreter and to functions 
# that interact strongly with the interpreter. It is always available.

class TodoList: #class/modules should begin with capital letter to distiguish with other objects.

    def __init__(self):
        self.tasks = [] #calling for the creation of instance variable 'tasks' list

    def add_task(self, task):
        self.tasks.append(task) #append/add an element to the 'tasks' list

    def remove_task(self, index):
        try:
            task = self.tasks.pop(index) #Python list pop() function removes elements at a specific index from the list.
            print(f"Task '{task}' removed")
        except IndexError: #if there is an index error add exception to the function.
            print("Invalid task Index.")
        
    def list_tasks(self):
        if self.tasks:
            print("Tasks: ")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks.")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(task + '\n')
            print(f"Tasks saved to '{filename}'.")
    
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f: # with open(filename, 'w') as f: opens the file for writing and assigns the resulting file object to the variable f, 
                                            #making it available within the with block. After the block ends, the file is automatically closed, and f goes out of scope.
                self.tasks = [line.strip() for line in f.readlines()]
            print(f"Tasks loaded from '{filename}'.")

        except FileNotFoundError:
            print(f"File '{filename}' not found.")

def main():
    todo_list = TodoList()

    while True: #conditional statement
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Save Tasks to File")
        print("5. Load Tasks from File")
        print("6. Quit")

        choice = input("\n Pick an Option: ")
        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("enter task index to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            todo_list.list_tasks()
        elif choice == '4':
            filename = input("enter filename to save tasks: ")
            todo_list.save_to_file(filename)
        elif choice == '5':
            filename = input("enter filename to load tasks: ")
            todo_list.load_from_file(filename)
        elif choice == '6':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__== "__main__":
    main()
