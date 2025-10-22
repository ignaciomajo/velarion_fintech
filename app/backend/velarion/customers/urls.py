from django.urls import path
from .views import ClientFeatureViewSet, ChurnPredictionViewSet

client_feature_list = ClientFeatureViewSet.as_view({'get': 'list', 'post': 'create'})
client_feature_detail = ClientFeatureViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
churn_prediction_list = ChurnPredictionViewSet.as_view({'get': 'list', 'post': 'create'})
churn_prediction_detail = ChurnPredictionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})


urlpatterns = [
    path('client-features/', client_feature_list, name='client_features_list'),
    path('client-features/<int:pk>/', client_feature_detail, name='client_features_detail'),
    path('churn-prediction/', churn_prediction_list, name='churn_prediction_list'),
    path('churn-prediction/<int:pk>/', churn_prediction_detail, name='churn_prediction_detail'),
]
