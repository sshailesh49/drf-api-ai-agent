from django.urls import path
from .views import CurrencyAgentView

urlpatterns = [
    path("convert/", CurrencyAgentView.as_view(), name="currency-agent"),
]

