
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
                    "CreditScore": 620,
                    "Geography": "France",
                    "Gender": "Male",
                    "Age": 35,
                    "Tenure": 5,
                    "Balance": 50000.0,
                    "NumOfProducts": 2,
                    "HasCrCard": 1,
                    "IsActiveMember": 0,
                    "EstimatedSalary": 70000.0,

                    "avg_tx_amount": 150.75,
                    "std_tx_amount": 45.3,
                    "days_since_last_tx": 10,
                    "tx_q1q2_rate_of_change": 0.15,
                    "tx_q2q3_rate_of_change": -0.05,

                    "avg_ss_duration": 45.0,
                    "std_ss_duration": 10.0,
                    "days_since_last_ss": 15,
                    "ss_q1q2_rate_of_change": 0.08,
                    "ss_q2q3_rate_of_change": 0.04,

                    "failed_ratio_spike_q2": 0.10,
                    "failed_ratio_spike_q3": 0.12,
                    "failed_ratio_volatility": 0.03
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

        proba = calcular_churn_probabilidad(data=df_in)
        
        try:
          result = {"probability": f"{proba:.2f}"}

        except Exception as e:
            # fallback se pipeline tiver interface diferente
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(result, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)