from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory "database"
tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Build API", "done": True}
]

@app.route("/")
def home():
    return "Flask API is running ✅"

#Get all Task
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

#Get Task by id
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"message": "Task not found"}), 404

#Post Task
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

#Put Task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        task["title"] = data.get("title", task["title"])
        task["done"] = data.get("done", task["done"])
        return jsonify(task)
    return jsonify({"message": "Task not found"}), 404

#Delete Task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Deleted"}), 204

if __name__ == "__main__":
    app.run(debug=True)
