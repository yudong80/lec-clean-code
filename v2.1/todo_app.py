import json

def add_task(tasks):
    desc = input("Enter task description: ")
    tasks.append({"description": desc, "done": False})
    save_tasks_json(tasks)
    print("Task added!")

def list_tasks(tasks):
    print("\nTask List:")
    for num, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{num}. [{status}] {task['description']}")

def done_task(tasks):
    num = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= num < len(tasks):
        tasks[num]["done"] = True
        save_tasks_json(tasks)
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def search_task(tasks):
    keyword = input("Enter keyword to search for: ")
    searched = []
    for task in tasks:
        if keyword.lower() in task["description"].lower():
            searched.append(task["description"])
    if searched:
        print("\nMatching tasks:")
        for num, task in enumerate(searched, start=1):
            print(f"{num}. {task}")
    else:
        print("No matching tasks found.")

def exit_app(tasks):
    save_tasks_json(tasks)
    print("Exiting the app.")

def save_tasks_json(tasks):
    with open("tasks.json", "w") as b:
        json.dump(tasks, b)

def load_tasks():
    tasks = []

    try:
        with open("tasks.json", "r") as b:
            tasks = json.load(b)
    except FileNotFoundError:
        pass
    return tasks

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do App\n")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Search task")
        print("5. Exit")

        select = input("Enter your choice: ")

        if select == "1":
            add_task(tasks)

        elif select == "2":
            list_tasks(tasks)

        elif select == "3":
            done_task(tasks)

        elif select == "4":
            search_task(tasks)

        elif select == "5":
            exit_app(tasks)
            break

        else:
            print("Invalid choice. Please choose a valid option.")

        save_tasks_json(tasks) 

if __name__ == "__main__":
    main()
