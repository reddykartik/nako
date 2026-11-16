# Useful commands

Run these from the repository root unless stated otherwise.

## Enter the Nix development shell

```bash
nix develop
```

## Start the application

```bash
podman compose -f deploy/compose.yaml up
```

## Start in the background

```bash
podman compose -f deploy/compose.yaml up -d
```

## View service status

```bash
podman compose -f deploy/compose.yaml ps
```

## View logs

```bash
podman compose -f deploy/compose.yaml logs
```

For a single service:

```bash
podman compose -f deploy/compose.yaml logs backend
podman compose -f deploy/compose.yaml logs frontend
```

## Stop the application

```bash
podman compose -f deploy/compose.yaml down
```

## Check the frontend

```bash
curl -i http://127.0.0.1:8080/
```

## Check the backend health/message endpoint

This works only if the backend is separately reachable from the host:

```bash
curl -i http://127.0.0.1:8000/
```

The supplied Compose configuration exposes backend port `8000` only within the Compose network, so this host request may not connect unless you separately publish or forward that port.

## Test the prediction route through Nginx

```bash
curl -i -X POST http://127.0.0.1:8080/api/predict \
  -H 'Content-Type: application/json' \
  -d '{"source_code":"print(\"hello\")"}'
```

## Check Git status

```bash
git status --short
```

## Check whether dataset and model files are tracked

```bash
git ls-files data models
```

The dataset and model artifacts are intentionally retained in version control in this project. Confirm that their licenses and redistribution terms permit this before publishing.
