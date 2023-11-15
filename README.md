# Basic Flask REST API

## Overview
This project is a basic REST API built using Flask, designed to handle tasks with various HTTP methods. The API allows users to create, retrieve, update, and delete tasks stored in a JSON file.

## Features
- **GET Requests:** Retrieve all tasks or a specific task by ID.
- **POST Requests:** Create a new task.
- **PATCH Requests:** Update an existing task.
- **DELETE Requests:** Delete a task by ID.
- **Error Handling:** Custom response for 404 Not Found errors.

## Installation
To use this API, clone this repository and ensure you have Flask installed.

```
pipenv install Flask
```

## Usage
Run the Flask app using:
```
python3 app.py
```

The API will be available at `http://127.0.0.1:5000/`.

### Endpoints

#### Get All Tasks
```
GET /todo/api/tasks
```

#### Get Task by ID
```
GET /todo/api/tasks/<task_id>
```

#### Create Task
```
POST /todo/api/tasks
```
Payload example:
```json
{
    "title": "Read a book",
    "description": "Get a book from the library and read it over a week"
}
```

#### Update Task by ID
```
PATCH /todo/api/tasks/<task_id>
```
Payload example:
```json
{
    "done": true
}
```

#### Delete Task by ID
```
DELETE /todo/api/tasks/<task_id>
```

## Testing
You can test the API endpoints using `curl` commands or any API client like Postman.

Example `curl` command:
```
curl -i http://127.0.0.1:5000/todo/api/tasks
```

## Contributing
Feel free to fork this project and submit pull requests for additional features or improvements.