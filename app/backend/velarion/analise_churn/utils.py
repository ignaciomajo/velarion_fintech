from django.conf import settings
import pickle

MODEL_PATH = settings.BASE_DIR / "analise_churn/ml/champion_model.pkl"
ENCODER_PATH = settings.BASE_DIR / "analise_churn/ml/one_hot_encoder.pkl"

_pipeline = None
_model = None

def get_pipeline():
    global _pipeline
    if _pipeline is None:
        with open(ENCODER_PATH, 'rb') as f:
            _pipeline = pickle.load(f)
    return _pipeline

def get_model():
    global _model
    if _model is None:
        with open(MODEL_PATH, 'rb') as f:
            _model = pickle.load(f)
    return _model
