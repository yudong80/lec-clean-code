import json

def main():
    a = []

    try:
        with open("tasks.json", "r") as b:
            a = json.load(b)
    except FileNotFoundError:
        pass

    while True:
        print("\nTo-Do App\n")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Search task")
        print("5. Exit")

        c = input("Enter your choice: ")

        if c == "1":
            d = input("Enter task description: ")
            a.append({"description": d, "done": False})
            with open("tasks.json", "w") as b:
                json.dump(a, b)
            print("Task added!")

        elif c == "2":
            print("\nTask List:")
            for e, f in enumerate(a, start=1):
                g = "Done" if f["done"] else "Not Done"
                print(f"{e}. [{g}] {f['description']}")

        elif c == "3":
            h = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= h < len(a):
                a[h]["done"] = True
                with open("tasks.json", "w") as b:
                    json.dump(a, b)
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif c == "4":
            i = input("Enter keyword to search for: ")
            j = []
            for k in a:
                if i.lower() in k["description"].lower():
                    j.append(k["description"])
            if j:
                print("\nMatching tasks:")
                for e, l in enumerate(j, start=1):
                    print(f"{e}. {l}")
            else:
                print("No matching tasks found.")

        elif c == "5":
            with open("tasks.json", "w") as b:
                json.dump(a, b)
            print("Exiting the app.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

        with open("tasks.json", "w") as b:
            json.dump(a, b)

if __name__ == "__main__":
    main()
