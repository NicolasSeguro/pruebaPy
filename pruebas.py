# create a tool in python to organize pending task list 

def add_task(task):
    with open('todo.txt', 'a') as file:
        file.write(task + '\n')
        file.close()
        print('Task added successfully!')
        print(f"Task added: {task}")
        print()

def view_tasks():
    with open('todo.txt', 'r') as file:
        tasks = file.readlines()
        file.close()
        print('Tasks:')
        for task in tasks:
            print(task.strip())

def remove_tasks():
    
    with open('todo.txt', 'r') as file:
        tasks = file.readlines()
        file.close()
    with open('todo.txt', 'w') as file:
        for task in tasks:
            if task.strip() != task:
                file.write(task)
        file.close()
        print('Tasks removed successfully!')
        print()

def main():
    while True:
        print('1. Add task')
        print('2. View tasks')
        print('3. Remove tasks')
        print('4. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            task = input('Enter task: ')
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_tasks()
        elif choice == '4':
            break
        else:
            print('Invalid choice')


