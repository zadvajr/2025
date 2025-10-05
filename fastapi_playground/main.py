from models import Task
from data_store import tasks
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running smoothly!"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task added successfully!"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            return {"message": f"Task with ID: {task_id} is updated successfully!"}
    return {"message": f"Task with ID: {task_id} not found!"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return {"message": f"Task with ID: {task_id} is deleted successfully!"}
    return {"message": f"Task with ID: {task_id} is not found!"}