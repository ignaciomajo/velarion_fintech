from .utils import get_pipeline, get_model

def calcular_churn_probabilidad(data):

    pipeline = get_pipeline()
    X_proc = pipeline.transform(data)

    model = get_model()
    prob = float(model.predict(X_proc).flatten()[0])

    return prob