# 📘 Assignment: Deploying a FastAPI Service

## 🎯 Objective

Prepare a FastAPI application for production-style deployment. In this assignment, you will configure environment-based settings, run FastAPI with a production server command, and package the app with Docker.

## 📝 Tasks

### 🛠️	Prepare the App for Deployment

#### Description
Use the starter code to create a deployment-ready FastAPI app that supports configurable settings and a health endpoint. The app should run cleanly in different environments without changing source code.

#### Requirements
Completed program should:

- Load `APP_NAME`, `APP_ENV`, and `APP_VERSION` from environment variables with safe defaults.
- Implement a `GET /` endpoint that returns app metadata from those settings.
- Implement a `GET /health` endpoint that returns a simple health status.
- Start the API with a production-style command using `uvicorn`.
- Keep the app runnable locally without Docker.


### 🛠️	Containerize and Run the Service

#### Description
Create deployment files so the API can run in a containerized environment. Build an image and run it while passing environment variables at startup.

#### Requirements
Completed program should:

- Include a `requirements.txt` file with required dependencies.
- Include a `Dockerfile` that installs dependencies and launches the app.
- Build and run the container successfully on port `8000`.
- Pass at least one environment variable at runtime (for example `APP_ENV=production`).
- Confirm `GET /health` returns a successful status from inside the running container.