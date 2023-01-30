from rest_framework import serializers
from .models import Whisky

class WhiskySerializer(serializers.ModelSerializer):
    class Meta:
        model = Whisky
        fields = '__all__'
