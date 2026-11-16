# Architecture

## Components

Nako has a browser frontend, an Nginx web server/reverse proxy, and a FastAPI backend that loads the trained scikit-learn pipeline.

```text
Browser
   |
   | HTTP: localhost:8080
   v
Nginx frontend
   |-- serves index.html
   |-- serves style.css
   |-- serves script.js
   |
   | /api/predict
   v
FastAPI backend
   |
   v
Saved scikit-learn pipeline
   |
   v
Prediction response
```

## Frontend

The static frontend files are located in `web/`:

- `web/index.html`
- `web/style.css`
- `web/script.js`

The browser accesses the frontend through Nginx.

## Nginx

The deployment configuration is in `deploy/nginx.conf`. Nginx serves the static frontend and forwards prediction requests under `/api/predict` to the backend service.

The Compose configuration publishes the frontend on host port `8080`. The backend listens on port `8000` inside the Compose network and is not directly published to the host by the supplied Compose file.

## Backend

The FastAPI application is in `src/nako/api.py`. It exposes:

- `GET /` — a simple service health/message response.
- `POST /predict` — accepts source code and returns the prediction result, or an HTTP 422 response when the prediction function returns an error object.

The prediction implementation is in `src/nako/predict.py`.

## Model

The serialized model is stored at:

```text
models/vulnerability_model.joblib
```

The model is a scikit-learn pipeline with raw-source TF-IDF and AST-derived TF-IDF feature branches, followed by `LinearSVC`.

## Container orchestration

`deploy/compose.yaml` defines the backend and frontend services on a shared bridge network. The frontend depends on the backend service and publishes port `8080` on the host.

Nix image definitions are located in `nix/backend-image.nix` and `nix/frontend-image.nix`. See [Deployment](deployment.md) for the current verification status.
