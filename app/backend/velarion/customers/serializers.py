from rest_framework import serializers
from .models import ClientFeature, ChurnPrediction

class ClientFeatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClientFeature
        fields = '__all__'
        


class ChurnPredictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChurnPrediction
        fields = ['id', 'cliente_id', 'modelo', 'prob_churn', 'data_execucao','riesgo']
