import joblib
from django.conf import settings
from tensorflow.keras.models import load_model

PIPELINE_PATH = settings.BASE_DIR / "analise_churn/ml/pipeline_churn.pkl"
MODEL_PATH = settings.BASE_DIR / "analise_churn/ml/rnn_churn_model.keras"

_pipeline = None
_model = None

def get_pipeline():
    global _pipeline
    if _pipeline is None:
        _pipeline = joblib.load(PIPELINE_PATH)
    return _pipeline

def get_model():
    global _model
    if _model is None:
        _model = load_model(MODEL_PATH)
    return _model
