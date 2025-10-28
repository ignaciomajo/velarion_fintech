from django.urls import path
from .views import PredictAPIView, user_profile

urlpatterns = [
    path('predict/', PredictAPIView.as_view(), name='predict'),
    path("user/me/", user_profile, name="user_profile"),
]
