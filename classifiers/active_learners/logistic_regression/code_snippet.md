```python
from sklearn.linear_model import LogisticRegression
from typing import List
# you can find further models here: https://scikit-learn.org/stable/supervised_learning.html#supervised-learning

YOUR_EMBEDDING: str = "text-classification-distilbert-base-uncased" # pick this from the options above
YOUR_MIN_CONFIDENCE: float = 0.8
YOUR_LABELS: List[str] = None # optional, you can specify a list to filter the predictions (e.g. ["label-a", "label-b"])

class MyLR(LearningClassifier):

    def __init__(self):
        self.model = LogisticRegression()

    @params_fit(
        embedding_name = YOUR_EMBEDDING, 
        train_test_split = 0.5 # we currently have this fixed, but you'll soon be able to specify this individually!
    )
    def fit(self, embeddings, labels):
        self.model.fit(embeddings, labels)

    @params_inference(
        min_confidence = YOUR_MIN_CONFIDENCE,
        label_names = YOUR_LABELS
    )
    def predict_proba(self, embeddings):
        return self.model.predict_proba(embeddings)
```