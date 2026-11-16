'''
$ train.py -- Mon Nov 16 13:00:49 IST 2026
Combine raw + ast tfidf tokens
'''
##
import ast
import joblib
from pathlib import Path
import pandas as pd
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.svm import LinearSVC
from sklearn.metrics import (
  accuracy_score,
  balanced_accuracy_score,
  roc_auc_score,
  classification_report,
  confusion_matrix
)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GroupShuffleSplit
##

## constants
SEED = 3
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "dataset.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "vulnerability_model.joblib"
##

## ast tokenizer
class ASTTokenExtractor(ast.NodeVisitor):
  def __init__(self):
    self.tokens = []

  def generic_visit(self, node):
    self.tokens.append(type(node).__name__)
    super().generic_visit(node)

def extract_features(source):
  tree = ast.parse(source)
  extractor = ASTTokenExtractor()
  extractor.visit(tree)
  return " ".join(extractor.tokens)

class ASTTokenTransformer(BaseEstimator, TransformerMixin):
  def fit(self, X, y=None):
    return self

  def transform(self, X):
    return [extract_features(source) for source in X]
##

def create_pipeline():
  ## Feature Union
  features = FeatureUnion([
    ("raw", TfidfVectorizer(
      token_pattern=r"(?u)\b\w+\b",
      analyzer="word",
      ngram_range=(1, 2),
    )),
    ("ast", Pipeline([
      ("extractor", ASTTokenTransformer()),
      ("tfidf", TfidfVectorizer(ngram_range=(1, 3))),
    ])),
  ])
  ##
  
  ## modelling
  model = Pipeline([
    ("features", features),
    ("svc", LinearSVC(
      C=10.0,
      max_iter=2000,
      random_state=SEED,
    )),
  ])
  ##
  return model

def main():
  ## loading dataset
  df = pd.read_csv(DATA_PATH)
  # print(df.info())
  # <class 'pandas.DataFrame'>
  # RangeIndex: 17692 entries, 0 to 17691
  # Data columns (total 4 columns):
  #  #   Column         Non-Null Count  Dtype
  # ---  ------         --------------  -----
  #  0   repo           17692 non-null  str
  #  1   source_code    17692 non-null  str
  #  2   patch          17692 non-null  str
  #  3   is_vulnerable  17692 non-null  int64
  # dtypes: int64(1), str(3)
  # memory usage: 553.0 KB
  # None
  ##

  ## splitting
  splitter = GroupShuffleSplit(
    n_splits=1,
    test_size=0.15,
    random_state=SEED,
  )
  
  train_val_idx, test_idx = next(splitter.split(
    df["source_code"],
    df["is_vulnerable"],
    groups=df["repo"],
  ))
  
  train_val = df.iloc[train_val_idx].reset_index(drop=True)
  test = df.iloc[test_idx].reset_index(drop=True)
  # print("\nTrain_Val size: ", train_val.shape)
  # print("Test size: ", test.shape)
  # 
  # Train_Val size:  (13811, 4)
  # Test size:  (3881, 4)
  ##
  model = create_pipeline()
  ## training
  print("TRAINING...")
  model.fit(train_val["source_code"], train_val["is_vulnerable"].values)
  y_combined = model.predict(test["source_code"])
  y_combined_score = model.decision_function(test["source_code"])
  y_test = test["is_vulnerable"].values
  print("\033[F\033[K", end="\r")
  print("TRAINING DONE!!")
  print("Accuracy: ", accuracy_score(y_test, y_combined))
  print("Balanaced accuracy: ", balanced_accuracy_score(y_test, y_combined))
  print("ROC-AUC score: ", roc_auc_score(y_test, y_combined_score))
  print("\n", classification_report(y_test, y_combined, zero_division=0))
  print(confusion_matrix(y_test, y_combined))
  # Accuracy:  0.7825302757021386
  # Balanaced Accuracy:  0.6993567270224235
  # ROC-AUC score:  0.8812965209884032
  # 
  #                precision    recall  f1-score   support
  # 
  #            0       0.76      0.98      0.85      2521
  #            1       0.91      0.42      0.58      1360
  # 
  #     accuracy                           0.78      3881
  #    macro avg       0.83      0.70      0.71      3881
  # weighted avg       0.81      0.78      0.76      3881
  # 
  # [[2464   57]
  #  [ 787  573]]
  # 
  ##
  ## saving model
  MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
  joblib.dump(model, MODEL_PATH)
  print(f"model saved at {MODEL_PATH}")
  # model saved at ../models/vulnerability_model.joblib
  ##

if __name__ == "__main__":
  main()

