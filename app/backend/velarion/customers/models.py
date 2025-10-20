from django.db import models

# Create your models here.
class ClientFeature(models.Model):
    id = models.BigIntegerField(primary_key=True)
    CreditScore = models.BigIntegerField(null=True, blank=True)
    Age = models.BigIntegerField(null=True, blank=True)
    Tenure = models.BigIntegerField(null=True, blank=True)
    Balance = models.FloatField(null=True, blank=True)
    NumOfProducts = models.BigIntegerField(null=True, blank=True)
    HasCrCard = models.BigIntegerField(null=True, blank=True)
    IsActiveMember = models.BigIntegerField(null=True, blank=True)
    EstimatedSalary = models.FloatField(null=True, blank=True)
    days_since_last_tx = models.BigIntegerField(null=True, blank=True)
    txs_avg_amount = models.FloatField(null=True, blank=True)
    amount_std = models.FloatField(null=True, blank=True)
    avg_cashout_amount = models.FloatField(null=True, blank=True)
    ratio_recent_vs_past_txs = models.FloatField(null=True, blank=True)
    ratio_recent_vs_past_amount = models.FloatField(null=True, blank=True)
    ratio_cashouts = models.FloatField(null=True, blank=True)
    ratio_transfers = models.FloatField(null=True, blank=True)
    inflation_pressure = models.FloatField(null=True, blank=True)
    days_since_last_ss = models.BigIntegerField(null=True, blank=True)
    total_ss_past30d = models.BigIntegerField(null=True, blank=True)
    total_ss_past90d = models.BigIntegerField(null=True, blank=True)
    avg_ss_per_wk = models.FloatField(null=True, blank=True)
    avg_ss_duration_min = models.FloatField(null=True, blank=True)
    std_ss_duration_min = models.FloatField(null=True, blank=True)
    ratio_ss_time_recent_vs_past = models.FloatField(null=True, blank=True)
    ratio_events_sessios = models.FloatField(null=True, blank=True)
    ratio_failed_ss = models.FloatField(null=True, blank=True)
    total_opened_push = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'client_feature'
        managed = False 


class ChurnPrediction(models.Model):
    cliente = models.ForeignKey(ClientFeature, on_delete=models.DO_NOTHING, db_column='cliente_id', related_name='predictions')
    modelo = models.CharField(max_length=50)
    prob_churn = models.FloatField()
    data_execucao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'churn_predictions'
        managed = False