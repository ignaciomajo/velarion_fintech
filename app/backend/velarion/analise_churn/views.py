
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import status
from .serializers import PredictSerializers, UserSerializer
from .service import calcular_churn_probabilidad
import pandas as pd
import numpy as np

class PredictAPIView(APIView):
 #   permission_classes = [IsAuthenticated]

    @extend_schema(
    request=PredictSerializers,
    responses={200: dict},
    examples=[
        OpenApiExample(
            "Exemplo de entrada",
            value={
                    "id": 1,
                    "CreditScore": -0.4364780387231289,
                    "Age": 0.2085538486731208,
                    "Tenure": -1.5553150795774706,
                    "Balance": -0.0126541355551008,
                    "NumOfProducts": -0.9192544052846996,
                    "HasCrCard": 0,
                    "IsActiveMember": 1,
                    "EstimatedSalary": 0.214729345168824,
                    "avg_tx_amount": -0.6562213520293952,
                    "std_tx_amount": 0.050831721006819,
                    "days_since_last_tx": -0.1502008296286636,
                    "tx_q1q2_rate_of_change": 0.5959465058455536,
                    "tx_q2q3_rate_of_change": 0.1757085377108986,
                    "avg_ss_duration": 0.5755584401001315,
                    "std_ss_duration": 0.0369260862083836,
                    "days_since_last_ss": -0.0469659019795534,
                    "ss_q1q2_rate_of_change": -0.0287812316113536,
                    "ss_q2q3_rate_of_change": 0.1430671365726679,
                    "failed_ratio_spike_q2": 1.4947779920259752,
                    "failed_ratio_spike_q3": -0.2114570151921181,
                    "failed_ratio_volatility": 0.6087499309056936,
                    "customerid": "15647311",
                    "surname": "Hill",
                    "Gender_Male": 0,
                    "Geography_Germany": 0,
                    "Geography_Spain": 1
                },
            request_only=True,
        ),
    ]
)

    
    def post(self, request):
        
        serializer = PredictSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        df_in = pd.DataFrame([data])

        proba = float(calcular_churn_probabilidad(data=df_in))
        print(proba)

        if proba > 0.75:
            riesgo = "Critical"
        elif (proba > 0.5) and (proba <= 0.75):
            riesgo = "Alto"
        elif (proba > 0.35) and (proba <= 0.5):
            riesgo = "Medio"
        else:
            riesgo = "Bajo"

        try:
          result = {"probability": f"{proba}",
                    "riesgo": riesgo
                    }

        except Exception as e:
            # fallback se pipeline tiver interface diferente
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(result, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)