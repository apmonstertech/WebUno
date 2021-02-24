from django.urls import path
from . import views

urlpatterns = [
    path('api/card/', views.CardListCreate.as_view() ),
]