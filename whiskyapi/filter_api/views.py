from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Whisky
from .serializers import WhiskySerializer
from rest_framework.filters import SearchFilter


class WhiskyViewSet(viewsets.ModelViewSet):
    queryset = Whisky.objects.filter()
    serializer_class = WhiskySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('short_description',)
    search_fields = ('short_description',)

