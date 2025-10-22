from rest_framework import serializers
from django.contrib.auth.models import User

class PredictSerializers(serializers.Serializer):

    CreditScore = serializers.FloatField()
    Age = serializers.FloatField()
    Tenure = serializers.FloatField()
    Balance = serializers.FloatField()
    NumOfProducts = serializers.FloatField()
    HasCrCard = serializers.IntegerField()
    IsActiveMember = serializers.IntegerField()
    EstimatedSalary = serializers.FloatField()
    days_since_last_tx = serializers.FloatField()
    txs_avg_amount = serializers.FloatField()
    amount_std = serializers.FloatField()
    avg_cashout_amount = serializers.FloatField()
    ratio_recent_vs_past_txs = serializers.FloatField()
    ratio_recent_vs_past_amount = serializers.FloatField()
    ratio_cashouts = serializers.FloatField()
    ratio_transfers = serializers.FloatField()
    inflation_pressure = serializers.FloatField()
    days_since_last_ss = serializers.FloatField()
    total_ss_past30d = serializers.FloatField()
    total_ss_past90d = serializers.FloatField()
    avg_ss_per_wk = serializers.FloatField()
    avg_ss_duration_min = serializers.FloatField()
    std_ss_duration_min = serializers.FloatField()
    ratio_ss_time_recent_vs_past = serializers.FloatField()
    ratio_events_sessios = serializers.FloatField()
    ratio_failed_ss = serializers.FloatField()
    total_opened_push = serializers.FloatField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]