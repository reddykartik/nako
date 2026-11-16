import ast
from sklearn.base import BaseEstimator, TransformerMixin

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
