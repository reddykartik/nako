import joblib
import ast
from pathlib import Path
from nako.features import ASTTokenTransformer

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "models" / "vulnerability_model.joblib"

model = joblib.load(MODEL_PATH)

def can_parse(source_code):
  try:
    ast.parse(source_code)
    return (True, None)
  except (SyntaxError, NameError, ValueError, TypeError) as error:
    return (False, error)

def predict(source_code):
  is_parsable, error = can_parse(source_code)
  if not is_parsable:
    return {
      "error": "Invalid Python source code",
      "line": error.lineno,
      "offset": error.offset,
      "message": error.msg,
    }
  prediction = model.predict([source_code])[0]
  decision_score = model.decision_function([source_code])[0]
  return {
    "prediction": int(prediction),
    "decision_score": float(decision_score),
  }


if __name__ == "__main__":
  source = '''
def add(a, b):
  return a + b
  '''
  res = predict(source)
  print(res)

