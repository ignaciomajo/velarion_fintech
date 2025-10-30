from .utils import  get_model

def calcular_churn_probabilidad(data):

    X_proc = data

    model = get_model()
    prob = float(model.predict_proba(X_proc)[:, 1][0])
    print(prob)
    return f"{prob:.3f}"