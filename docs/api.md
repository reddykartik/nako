# API Documentation

## 1. Overview

The backend exposes a REST API using FastAPI.

The API accepts Python source code and returns a binary vulnerability prediction with a decision score.

## 2. Endpoint

### POST /predict

Accepts a source-code sample.

Request:

```http
POST /predict
Content-Type: application/json
```

Request body:

```json
{
  "source_code": "print('Hello, world!')"
}
```

Response:

```json
{
  "prediction": 0,
  "decision_score": -1.2030093470319467
}
```

### Response fields

| Field | Type | Description |
|---|---|---|
| `prediction` | Integer | Predicted class |
| `decision_score` | Number | Linear classifier decision score |

Prediction labels:

- `0`: Non-vulnerable.
- `1`: Vulnerable.

The decision score is not a probability.

## 3. Frontend Endpoint

The browser submits requests to:

```text
POST /api/predict
```

Nginx forwards them to the backend's `/predict` endpoint.

The browser-facing endpoint uses the frontend's origin.

## 4. Running the API Independently

Inside the Nix development environment:

```bash
nix develop
```

Run:

```bash
python -m uvicorn nako.api:app \
  --app-dir src \
  --host 127.0.0.1 \
  --port 8000
```

## 5. Testing the API

```bash
curl -X POST \
  http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"source_code": "print(1 + 1)"}'
```

Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

When running through Compose, access the browser-facing endpoint on port 8080.

## 6. Error Handling

The API should return appropriate HTTP error codes for invalid request bodies and internal failures.

The exact validation and exception handling behavior is defined in `src/nako/api.py`.

Do not expose internal stack traces or sensitive server information to the browser.

---

