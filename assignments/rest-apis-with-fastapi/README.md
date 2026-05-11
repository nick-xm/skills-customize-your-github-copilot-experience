# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework. In this assignment, you will practice creating endpoints, working with request and response data, and organizing API logic in Python.

## 📝 Tasks

### 🛠️	Create Basic API Endpoints

#### Description
Use FastAPI to build an application with a few basic endpoints. Start by creating a root route and a route that returns a list of items so you can verify that your API is running correctly.

#### Requirements
Completed program should:

- Create a FastAPI application instance.
- Add a `GET /` endpoint that returns a short welcome message.
- Add a `GET /items` endpoint that returns a list of sample items.
- Return data as JSON responses.
- Run successfully with a FastAPI-compatible server such as `uvicorn`.


### 🛠️	Add Item Lookup and Creation

#### Description
Extend your API so users can retrieve a single item by ID and create a new item with a `POST` request. Use an in-memory list for storage so you can focus on API design instead of database setup.

#### Requirements
Completed program should:

- Add a `GET /items/{item_id}` endpoint that returns one item by ID.
- Return a clear error message when the requested item does not exist.
- Add a `POST /items` endpoint that accepts item data and stores it in memory.
- Validate incoming data using a FastAPI model.
- Return the newly created item in the response.