from rest_framework import generics
from .models import Snack
from .serializers import SnackSerializer

    
class SnackListView(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer