# Nako Technical Documentation

---
# System Architecture

## 1. Overview

Nako is structured as a small client-server application with a machine-learning inference backend.

The system separates the user interface, HTTP routing and machine-learning inference into independent components.

## 2. Components

### Frontend

Location: `web/`

Technologies:
- HTML
- CSS
- JavaScript

Responsibilities:
- Accept Python source code from the user.
- Submit prediction requests.
- Display the returned classification.
- Display the model decision score.

The frontend does not perform model inference.

### Reverse Proxy

Location: `deploy/nginx.conf`

Technology: Nginx.

Responsibilities:
- Serve static frontend files.
- Accept browser HTTP requests.
- Forward prediction requests to the backend.
- Provide a single entry point for the application.

### Backend

Location: `src/nako/`

Technology: FastAPI.

Responsibilities:
- Accept source-code submissions.
- Validate request data.
- Load the serialized prediction pipeline.
- Extract source-code features.
- Perform classification.
- Return predictions as JSON.

### Machine Learning Model

Location: `models/vulnerability_model.joblib`

The serialized artifact contains the trained inference pipeline.

It is loaded by the backend and reused for prediction requests.

## 3. Request Flow

A typical prediction request follows these steps:

1. The user enters Python source code.
2. The browser sends a POST request to `/api/predict`.
3. Nginx forwards the request to the backend.
4. FastAPI receives the source code.
5. The prediction pipeline extracts features.
6. The classifier generates a prediction.
7. The backend returns a JSON response.
8. The browser displays the result.

## 4. Deployment Architecture

The application uses two container images:

| Service | Responsibility | Internal port |
|---|---|---:|
| Frontend | Nginx and static files | 80 |
| Backend | FastAPI inference | 8000 |

The frontend is exposed to the host on port 8080 through Compose.

The backend is accessed through the internal container network.

## 5. Design Decisions

### Separate frontend and backend

Separating the services allows the frontend and inference backend to be developed and deployed independently.

### Nginx reverse proxy

The reverse proxy provides a single browser-facing entry point and avoids requiring the frontend to communicate directly with a separately exposed backend port.

### Serialized inference pipeline

The model is serialized so that training is not required every time the application starts.

### Nix-based builds

Nix describes the development environment and container image construction declaratively.

This reduces dependence on manually installed packages and machine-specific configuration.

---

