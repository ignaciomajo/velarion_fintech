from rest_framework import serializers
from .models import ClientFeature, ChurnPrediction

class ClientFeatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClientFeature
        fields = '__all__'
        


class ChurnPredictionSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(source='cliente.customerid', read_only=True)
  

    class Meta:
        model = ChurnPrediction
        fields = ['id', 'customer_id','modelo', 'prob_churn', 'data_execucao','riesgo']
