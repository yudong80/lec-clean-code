import json

def add_task(tasks):
    d = input("Enter task description: ")
    tasks.append({"description": d, "done": False})
    with open("tasks.json", "w") as b:
        json.dump(tasks, b)
    print("Task added!")

def list_tasks(tasks):
    print("\nTask List:")
    for e, f in enumerate(tasks, start=1):
        g = "Done" if f["done"] else "Not Done"
        print(f"{e}. [{g}] {f['description']}")

def done_task(tasks):
    h = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= h < len(tasks):
        tasks[h]["done"] = True
        with open("tasks.json", "w") as b:
            json.dump(tasks, b)
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def search_task(tasks):
    i = input("Enter keyword to search for: ")
    j = []
    for k in tasks:
        if i.lower() in k["description"].lower():
            j.append(k["description"])
    if j:
        print("\nMatching tasks:")
        for e, l in enumerate(j, start=1):
            print(f"{e}. {l}")
    else:
        print("No matching tasks found.")

def exit_app(tasks):
    with open("tasks.json", "w") as b:
        json.dump(tasks, b)
    print("Exiting the app.")

def main():
    tasks = []

    try:
        with open("tasks.json", "r") as b:
            tasks = json.load(b)
    except FileNotFoundError:
        pass

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

        with open("tasks.json", "w") as b:
            json.dump(tasks, b)

if __name__ == "__main__":
    main()
