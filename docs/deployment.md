# Deployment Guide

## 1. Overview

Nako is deployed as two containerized services:

- Backend: FastAPI inference service.
- Frontend: Nginx static web server and reverse proxy.

The images are constructed using Nix and run using Podman Compose.

## 2. Build the Images

Enter the development environment:

```bash
nix develop
```

Build backend:

```bash
nix build .#backend -o result-backend
```

Build frontend:

```bash
nix build .#frontend -o result-frontend
```

Inspect outputs:

```bash
file result-backend
file result-frontend
```

## 3. Load Images into Podman

```bash
podman load -i result-backend
podman load -i result-frontend
```

Inspect available images:

```bash
podman images
```

If Podman reports that `policy.json` is missing, inspect the local containers configuration before attempting to load the archives.

## 4. Start Services

```bash
podman compose -f deploy/compose.yaml up --force-recreate
```

To run in the background:

```bash
podman compose -f deploy/compose.yaml up -d
```

View running containers:

```bash
podman ps
```

View logs:

```bash
podman compose -f deploy/compose.yaml logs
```

Follow logs:

```bash
podman compose -f deploy/compose.yaml logs -f
```

View individual service logs:

```bash
podman compose -f deploy/compose.yaml logs backend
podman compose -f deploy/compose.yaml logs frontend
```

## 5. Verify Deployment

Open:

```text
http://127.0.0.1:8080/
```

Verify the frontend response:

```bash
curl -I http://127.0.0.1:8080/
```

Verify prediction through Nginx:

```bash
curl -X POST \
  http://127.0.0.1:8080/api/predict \
  -H "Content-Type: application/json" \
  -d '{"source_code": "print(1 + 1)"}'
```

Expected behavior:

- Frontend returns HTTP 200.
- Backend starts successfully.
- Prediction request reaches the backend.
- Backend returns HTTP 200 with prediction data.

## 6. Stop Services

```bash
podman compose -f deploy/compose.yaml down
```

This stops and removes the Compose-managed containers and network.

It does not delete the source datasets or model artifact.

## 7. Rebuild After Changes

After changing the backend:

```bash
nix build .#backend -o result-backend
podman load -i result-backend
podman compose -f deploy/compose.yaml up --force-recreate
```

After changing the frontend:

```bash
nix build .#frontend -o result-frontend
podman load -i result-frontend
podman compose -f deploy/compose.yaml up --force-recreate
```

If both change, rebuild and load both.

## 8. Troubleshooting

### Port already in use

Check processes:

```bash
ss -ltnp
```

Inspect container status:

```bash
podman ps -a
```

### Container logs

```bash
podman compose -f deploy/compose.yaml logs -f
```

### Inspect images

```bash
podman images
```

### Inspect networks

```bash
podman network ls
```

### Recreate services

```bash
podman compose -f deploy/compose.yaml down
podman compose -f deploy/compose.yaml up --force-recreate
```

### Nginx configuration

Inspect the Nginx configuration inside the frontend image and validate it using the Nginx configuration test when appropriate.

### Backend startup

Verify that:

- The model artifact exists in the image.
- Python dependencies are available.
- The application module can be imported.
- Port 8000 is available inside the container.

---

