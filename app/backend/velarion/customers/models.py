from django.db import models

# Create your models here.
class ClientFeature(models.Model):
    id = models.BigAutoField(primary_key=True)
    customerid =  models.CharField(max_length=50, null=True, blank=True)
    surname = models.CharField(max_length=50, null=True, blank=True)
    # Campos originais compatíveis com o serializer
    creditscore = models.FloatField(null=True, blank=True)
    geography_spain = models.FloatField(null=True, blank=True)
    geography_germany = models.FloatField(null=True, blank=True)
    gender_male = models.FloatField(null=True, blank=True)
    age = models.FloatField(null=True, blank=True)
    tenure = models.FloatField(null=True, blank=True)
    balance = models.FloatField(null=True, blank=True)
    numofproducts = models.FloatField(null=True, blank=True)
    hascrcard = models.FloatField(null=True, blank=True)
    isactivemember = models.FloatField(null=True, blank=True)
    estimatedsalary = models.FloatField(null=True, blank=True)

    # Transações (tx)
    avg_tx_amount = models.FloatField(null=True, blank=True)
    std_tx_amount = models.FloatField(null=True, blank=True)
    days_since_last_tx = models.FloatField(null=True, blank=True)
    tx_q1q2_rate_of_change = models.FloatField(null=True, blank=True)
    tx_q2q3_rate_of_change = models.FloatField(null=True, blank=True)

    # Sessões (ss)
    avg_ss_duration = models.FloatField(null=True, blank=True)
    std_ss_duration = models.FloatField(null=True, blank=True)
    days_since_last_ss = models.FloatField(null=True, blank=True)
    ss_q1q2_rate_of_change = models.FloatField(null=True, blank=True)
    ss_q2q3_rate_of_change = models.FloatField(null=True, blank=True)

    # Indicadores de falha
    failed_ratio_spike_q2 = models.FloatField(null=True, blank=True)
    failed_ratio_spike_q3 = models.FloatField(null=True, blank=True)
    failed_ratio_volatility = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"ClientFeature({self.id})"

    class Meta:
        db_table = 'client_feature'
         


class ChurnPrediction(models.Model):
    cliente = models.ForeignKey(ClientFeature, on_delete=models.DO_NOTHING, db_column='cliente_id', related_name='predictions')
    modelo = models.CharField(max_length=100)
    prob_churn = models.FloatField()
    data_execucao = models.DateTimeField(auto_now_add=True)
    riesgo = models.CharField(max_length=100,null=True, blank=True)

    class Meta:
        db_table = 'churn_predictions'