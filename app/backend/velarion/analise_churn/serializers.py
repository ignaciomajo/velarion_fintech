from rest_framework import serializers
from django.contrib.auth.models import User

class PredictSerializers(serializers.Serializer):

    CreditScore = serializers.FloatField()
    Geography = serializers.CharField()          
    Gender = serializers.CharField()             
    Age = serializers.FloatField()
    Tenure = serializers.FloatField()
    Balance = serializers.FloatField()
    NumOfProducts = serializers.FloatField()
    HasCrCard = serializers.IntegerField()
    IsActiveMember = serializers.IntegerField()
    EstimatedSalary = serializers.FloatField()

    avg_tx_amount = serializers.FloatField()
    std_tx_amount = serializers.FloatField()
    days_since_last_tx = serializers.FloatField()
    tx_q1q2_rate_of_change = serializers.FloatField()
    tx_q2q3_rate_of_change = serializers.FloatField()

    avg_ss_duration = serializers.FloatField()
    std_ss_duration = serializers.FloatField()
    days_since_last_ss = serializers.FloatField()
    ss_q1q2_rate_of_change = serializers.FloatField()
    ss_q2q3_rate_of_change = serializers.FloatField()

    failed_ratio_spike_q2 = serializers.FloatField()
    failed_ratio_spike_q3 = serializers.FloatField()
    failed_ratio_volatility = serializers.FloatField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]