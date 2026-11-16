from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from nako.predict import predict

app = FastAPI(
  title="nako",
  description="Python vulnerability detection API",
  version="0.1.0",
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=[
    "http://localhost:3000",
    "http://127.0.0.1:3000",
  ],
  allow_credentials=False,
  allow_methods=["*"],
  allow_headers=["*"],
)

class Request(BaseModel):
  source_code: str

@app.get("/")
def home():
  return {"message": "nako is running"}

@app.post("/predict")
def prediction(request: Request):
  res = predict(request.source_code) 
  if "error" in res:
    return JSONResponse(
      status_code=422,
      content=res,
    )
  return res

