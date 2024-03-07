from django.contrib import admin
from django.urls import path, include  # 👈 1. add this
# delete
urlpatterns = [
    path ('', include ('tradingapp.urls'))
]