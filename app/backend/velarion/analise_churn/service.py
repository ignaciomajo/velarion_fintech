from .utils import get_pipeline, get_model

def calcular_churn_probabilidad(data):

    pipeline = get_pipeline()
    X_proc = pipeline.transform(data)

    model = get_model()
    prob = float(model.predict_proba(X_proc)[:, 1][0])
    print(prob)
    return f"{prob:.3f}"