from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM tasks")
print(cursor.fetchall())
app = FastAPI()


class Task(BaseModel):
    title: str


tasks = [
    {"id": 1, "title": "study python"},
    {"id": 2, "title": "go to pool"},
]

@app.get("/tasks")
def get_tasks():

    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    conn.close()

    return tasks


@app.post("/tasks")
def add_task(task: Task):

    new_task = {"id": len(tasks) + 1, "title": task.title}

    tasks.append(new_task)

    return new_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}

    return {"message": "Task not found"}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_name: str):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_name
            return task

    return {"message": "Task not found"}


@app.get("/tasks/{task_id}")
def show_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return {"message": "Task not found"}
