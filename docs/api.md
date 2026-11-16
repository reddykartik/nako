# API

The API is implemented in `src/nako/api.py` using FastAPI.

## Base URL

When using the Compose deployment, access the frontend through:

```text
http://localhost:8080
```

The browser sends prediction requests to Nginx under `/api/predict`. Nginx forwards the request to the backend's `/predict` endpoint.

The backend listens on port `8000` inside the Compose network. The supplied Compose file does not publish this port directly to the host.

## Health/message endpoint

```http
GET /
```

Example response:

```json
{
  "message": "nako is running"
}
```

## Prediction endpoint

The backend endpoint is:

```http
POST /predict
Content-Type: application/json
```

Request body:

```json
{
  "source_code": "print('hello')"
}
```

The request schema requires a string field named `source_code`.

The frontend-facing Nginx route is:

```text
POST /api/predict
```

Example backend request using curl, when the backend is reachable at the host:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H 'Content-Type: application/json' \
  -d '{"source_code":"print(\"hello\")"}'
```

The prediction response fields depend on `src/nako/predict.py`. Confirm that file before documenting a complete response schema. A recorded example response was:

```json
{
  "prediction": 1,
  "decision_score": 3.086031058737967
}
```

A prediction value of `0` corresponds to non-vulnerable and `1` to vulnerable, according to the training target definition.

If the prediction function returns a dictionary containing an `error` key, the API returns it with HTTP status `422`.

## Important note

The classifier is experimental. Its prediction is not a security guarantee. In the recorded test results, vulnerable-class recall was approximately 0.42.
