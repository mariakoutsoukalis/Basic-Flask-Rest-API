from json import loads, dump
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

PATH_TO_DATASET = "/Users/mariacristel/Desktop/Basic-Flask-Rest-API/server/data/tasks.json"
with open(PATH_TO_DATASET, "r") as fr:
    tasks = loads(fr.read())["tasks"]
#print(tasks)
#print (type(tasks))

#Verify Flask is running efficiently

@app.route("/", methods=["GET"])
def index():
    return {"message": "Hello! Welcome to my basic REST API"}

#Verify Data is integrated into API

"""
Test with the following command:
    curl -i http://127.0.0.1:5000/todo/api/tasks
"""
@app.route("/todo/api/tasks", methods=["GET"])
def get_tasks():
    return tasks, 201

#GET Request
"""
Test with the following command:
    curl -i http://127.0.0.1:5000/todo/api/tasks/1
"""
@app.route("/todo/api/tasks/<int:task_id>", methods=["GET"])
def get_task_by_task_id(task_id):
    task = [task for task in tasks if task["id"] == int(task_id)]
    if len(task) == 0:
        abort(404)
    return jsonify({"task": task[0]}), 201

#POST Request
"""
Test with the following command:
    curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book","description":"Get a book from the library and read it over a week"}' http://127.0.0.1:5000/todo/api/tasks
```
"""
@app.route("/todo/api/tasks", methods=["POST"])
def create_task():
    if not request.json or not "title" in request.json:
        abort(400)
    with open(PATH_TO_DATASET, "w") as fw:
        task = {
            "id": len(tasks) + 1,
            "title": request.json["title"],
            "description": request.json.get("description", ""),
            "done": False
        }
        tasks.append(task)
        dump({"tasks": tasks}, fw, indent=4)
    return jsonify({"task": task}), 201

#PATCH Request
"""
Test with the following command:
    curl -i -H "Content-Type: application/json" -X PATCH -d '{"done":true}' http://127.0.0.1:5000/todo/api/tasks/2
"""
@app.route("/todo/api/tasks/<int:task_id>", methods=["PATCH"])
def update_task_by_task_id(task_id):
    task = [task for task in tasks if task["id"] == int(task_id)]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if "title" in request.json and type(request.json["title"]) is not str:
        abort(400)
    if "description" in request.json and type(request.json["description"]) is not str:
        abort(400)
    if "done" in request.json and type(request.json["done"]) is not bool:
        abort(400)
    with open("server/data/tasks.json", "w") as fw:
        task[0]["title"] = request.json.get("title", task[0]["title"])
        task[0]["description"] = request.json.get("description", task[0]["description"])
        task[0]["done"] = request.json.get("done", task[0]["done"])
        dump({"tasks": tasks}, fw, indent=4)
    return jsonify({"task": task[0]}), 201


#DELETE Request
"""
Test with the following command:
    curl -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/todo/api/tasks/3
"""
@app.route("/todo/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task_by_task_id(task_id):
    task = [task for task in tasks if task["id"] == int(task_id)]
    if len(task) == 0:
        abort(404)
    with open("server/data/tasks.json", "w") as fw:
        tasks.remove(task[0])
        dump({"tasks": tasks}, fw, indent=4)
    return jsonify(task[0]), 201

#404 Error Handling
"""
Test with the following command:
    curl -i http://127.0.0.1:5000/whoooooooooo
"""
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not Found!"}), 404)

if __name__ == "__main__":
    app.run(debug=True, port=5000)