from rest_framework import generics
from .models import Developer
from .serializer import DeveloperSerializer


class DeveloperView(generics.ListCreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
