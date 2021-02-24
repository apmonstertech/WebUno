from .models import Card
from .serializers import CardSerializer
from rest_framework import generics

class CardListCreate(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
