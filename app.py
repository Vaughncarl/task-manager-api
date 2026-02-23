from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "description": data.get("description"),
        "completed": False,
        "created_at": datetime.now().isoformat()
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = request.json.get("completed", task["completed"])
            return jsonify(task)
    return {"message": "Task not found"}, 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return {"message": "Task deleted"}

if __name__ == "__main__":
    app.run(debug=True)
