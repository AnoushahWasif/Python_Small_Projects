import sqlite3

def add_task(task_title, task_description, task_status):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    # Execute SQL INSERT statement to add a new task
    cursor.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)", (task_title, task_description, task_status))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_task("Task 1", "Water the plants", "Pending")
    add_task("Task 2", "Buy groceries", "Completed")
    add_task("Task 3", "Clean the house", "Pending")
    add_task("Task 4", "Take out the trash", "In Progress")
    add_task("Task 5", "Walk the dog", "Pending")
    add_task("Task 6", "Prepare dinner", "Completed")
    add_task("Task 7", "Do laundry", "Pending")
    add_task("Task 8", "Read a book", "Pending")
    add_task("Task 9", "Exercise", "In Progress")
    add_task("Task 10", "Watch a movie", "Pending")
    print("Tasks added successfully.")