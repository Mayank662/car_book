from rest_framework import serializers
from .models import UserData

class UserDataSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length = 20)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length = 10)
    pickup_date = serializers.DateField()
    dropoff_date = serializers.DateField()
    pickup_time = serializers.TimeField()
    dropoff_time = serializers.TimeField()
    pickup_add = serializers.CharField()
    dropoff_add = serializers.CharField()

    class Meta:
        model = UserData
        fields = ('__all__')