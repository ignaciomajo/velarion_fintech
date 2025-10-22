
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
                "Age": 35,
                "Tenure": 5,
                "Balance": 50000.0,
                "NumOfProducts": 2,
                "HasCrCard": 1,
                "IsActiveMember": 0,
                "EstimatedSalary": 70000.0,
                "days_since_last_tx": 10,
                "txs_avg_amount": 150.75,
                "amount_std": 45.3,
                "avg_cashout_amount": 200.0,
                "ratio_recent_vs_past_txs": 1.2,
                "ratio_recent_vs_past_amount": 1.1,
                "ratio_cashouts": 0.3,
                "ratio_transfers": 0.7,
                "inflation_pressure": 0.02,
                "days_since_last_ss": 15,
                "total_ss_past30d": 8,
                "total_ss_past90d": 20,
                "avg_ss_per_wk": 2.5,
                "avg_ss_duration_min": 45,
                "std_ss_duration_min": 10,
                "ratio_ss_time_recent_vs_past": 0.9,
                "ratio_events_sessios": 0.8,
                "ratio_failed_ss": 0.1,
                "total_opened_push": 12
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