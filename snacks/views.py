from rest_framework import generics,permissions
from .models import Snack
from .serializers import SnackSerializer
from .permissions import IsAuthorOrReadOnly
    
class SnackListView(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)   


class SnackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (IsAuthorOrReadOnly,)   