from fastapi import FastAPI, HTTPException, status
import sqlite3

app = FastAPI()
conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL
)
""")

cursor.execute("SELECT COUNT(*) FROM tasks")
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        [
            ("Learn FastAPI", 0),
            ("Build CRUD API", 0),
            ("Push to GitHub", 0),
        ]
    )
    conn.commit()


@app.get("/")
def home():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": [
            "/tasks",
            "/health"
        ]
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    tasks = []
    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "done": bool(row[2])
        })

    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    row = cursor.fetchone()

    if row:
        return {
            "id": row[0],
            "title": row[1],
            "done": bool(row[2])
        }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: dict):

    if "title" not in task or task["title"].strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title is required"
        )

    cursor.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (task["title"], 0)
    )
    conn.commit()

    task_id = cursor.lastrowid

    return {
        "id": task_id,
        "title": task["title"],
        "done": False
    }


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: dict):

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()

    if not row:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    title = updated_task.get("title", row[1])
    done = updated_task.get("done", bool(row[2]))

    cursor.execute(
        "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
        (title, int(done), task_id)
    )
    conn.commit()

    return {
        "id": task_id,
        "title": title,
        "done": done
    }


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()

    if not row:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

    return