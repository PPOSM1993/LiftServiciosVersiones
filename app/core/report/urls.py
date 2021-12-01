from django.urls import path
from core.report.views import *

urlpatterns = [
    path('buy/', ReportBuyView.as_view(), name="buy_report"),
]
