from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from rest_framework.pagination import PageNumberPagination
from .models import ClientFeature, ChurnPrediction
from .serializers import ClientFeatureSerializer, ChurnPredictionSerializer

# Create your views here.

class ClientFeaturePagination(PageNumberPagination):
    page_size = 25  
    page_size_query_param = 'page_size'  
    max_page_size = 50

class ClientFeatureViewSet(viewsets.ModelViewSet):
    queryset = ClientFeature.objects.all()
    serializer_class = ClientFeatureSerializer
    pagination_class = ClientFeaturePagination

class ChurnPredictionPagination(PageNumberPagination):
    page_size = 25  
    page_size_query_param = 'page_size'  
    max_page_size = 50

class ChurnPredictionViewSet(viewsets.ModelViewSet):
    queryset = ChurnPrediction.objects.all()
    serializer_class = ChurnPredictionSerializer
    pagination_class = ChurnPredictionPagination

    @action(detail=False, methods=['get'])
    def resumen_riesgo(self, request):
        data = (
            ChurnPrediction.objects
            .values('riesgo')
            .annotate(total=Count('riesgo'))
            .order_by('-total')
        )
        return Response(list(data))

