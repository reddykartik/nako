# Deployment

## Services

The Compose file is:

```text
deploy/compose.yaml
```

It defines:

- `backend` — image `localhost/nako-backend:latest`, listening on port `8000` inside the Compose network.
- `frontend` — image `localhost/nako-frontend:latest`, publishing host port `8080` to container port `80`.

Both services join the `nako-network` bridge network. The frontend depends on the backend.

## Start and stop

From the repository root, inside the configured development environment:

```bash
nix develop
podman compose -f deploy/compose.yaml up
```

Open:

```text
http://localhost:8080
```

Stop the services:

```bash
podman compose -f deploy/compose.yaml down
```

## Nginx

- `deploy/nginx.conf` is copied into the frontend image and used by the Nginx container.
- `deploy/nginx-dev.conf` is the development configuration used when running Nginx locally.

The frontend serves the static files and proxies `/api/predict` to the backend service. Because the browser uses the same origin for the frontend and the `/api/predict` path, browser requests through this reverse proxy do not require cross-origin access.

## Nix image definitions

The image definitions are:

```text
nix/backend-image.nix
nix/frontend-image.nix
```

They are intended to build the backend and frontend container images.

## Verification status and caveat

The application was observed running through Podman Compose: the frontend, CSS and JavaScript returned HTTP 200, and the frontend prediction route and backend prediction endpoint returned HTTP 200.

However, a separate attempt to load the freshly built Nix image archive with `podman load -i result` failed with an image-format/policy error. Therefore, successful application startup does **not** by itself prove that the latest Nix-built image archives were loaded and used. Do not claim a fully verified clean image-build-and-load workflow until that process has been successfully repeated and confirmed.

Podman also emitted a warning that the storage driver was not explicitly set and was selected automatically. This was a warning, not the reported cause of the application startup.

## Reproducibility checklist

Before claiming reproducible deployment, verify all of the following on a clean environment:

1. Build both Nix image outputs successfully.
2. Identify the exact generated image archive paths.
3. Load those archives into Podman successfully.
4. Confirm the expected image tags are present.
5. Start Compose using those exact images.
6. Verify the frontend, static assets, and prediction request.
7. Record the exact commands and successful output.

Do not state that this checklist is complete until each step has been performed successfully.
