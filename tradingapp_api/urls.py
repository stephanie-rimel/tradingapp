from django.urls import path

from .views import (
    TradingListApiView,
    TradingDetailApiView
)

urlpatterns = [
    path('api/<int:trading_id>/', TradingDetailApiView.as_view ()),
    path('api', TradingListApiView.as_view()),

]