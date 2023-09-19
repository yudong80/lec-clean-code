from unittest import TestCase, main
import todo_app as app

class MyTests(TestCase):
    def test_clear_tasks(self):
        app.clear_tasks()
        tasks = app.load_tasks()

        self.assertEqual(0, len(tasks))

    def test_add_tasks(self):
        tasks = app.load_tasks()
        count_before = len(tasks)

        sample = {"description": "1111", "done": False}
        app.add_task(tasks, sample)
        app.save_tasks_json(tasks)
              
        tasks_after = app.load_tasks()
        self.assertEqual(count_before + 1 , len(tasks_after))


if __name__ == '__main__':
    main()