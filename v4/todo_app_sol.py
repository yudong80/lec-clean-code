import json
from task import Task


def add_task(tasks, desc):
    # 할일을 추가
    # 형식은 {'description': XXX , 'done': True/False}
    tasks.append(Task(desc))
    save_tasks_json(tasks)
    print("Task added!")


def list_tasks(tasks):
    print("\nTask List:")
    for num, task in enumerate(tasks, start=1):
        print(f"{num}. {task}")


def done_task(tasks, num):
    # 할일 완료
    # 'done' 속성을 True로 변경
    if 0 <= num < len(tasks):
        tasks[num].mark_as_done()
        save_tasks_json(tasks)
        print("Task marked as done!")
    else:
        print("Invalid task number.")


def search_task(tasks, keyword):
    # 할일 검색
    # 'description' 속성을 검색
    searched = []
    for task in tasks:
        if keyword.lower() in task.description.lower():
            searched.append(task)
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
        json.dump([vars(task) for task in tasks], b)


def load_tasks():
    tasks = []

    try:
        with open("tasks.json", "r") as b:
            tasks_data = json.load(b)
            for task_data in tasks_data:
                task = Task(**task_data)
                tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks


def clear_tasks():
    tasks = []
    save_tasks_json(tasks)


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
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif select == "2":
            list_tasks(tasks)
        elif select == "3":
            num = int(input("Enter task number to mark as done: ")) - 1
            done_task(tasks, num)
        elif select == "4":
            keyword = input("Enter search keyword: ")
            search_task(tasks, keyword)
        elif select == "5":
            exit_app(tasks)
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
