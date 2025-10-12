from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status
from .serializers import PredictSerializers
from .service import calcular_churn_probabilidad
import pandas as pd

class PredictAPIView(APIView):
   # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PredictSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        df_in = pd.DataFrame([data])

        proba = calcular_churn_probabilidad(data=df_in)
        
        try:
          result = {
            "probability": proba
            }

        except Exception as e:
            # fallback se pipeline tiver interface diferente
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(result, status=status.HTTP_200_OK)