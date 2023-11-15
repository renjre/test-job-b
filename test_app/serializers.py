from rest_framework import serializers
from test_app.models import *


class UserLoginSerializer( serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'gender',
            'age',
            'country',
            'city'
            ]

class CountrySerializer(serializers.ModelSerializer):
    cities = serializers.SerializerMethodField()

    def get_cities(self, obj):
        # Assuming the related name in the City model is 'city'
        cities = obj.city_set.values_list('name', flat=True)
        return list(cities)

    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "cities"
            ]

