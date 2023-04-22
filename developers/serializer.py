from rest_framework import serializers
from .models import Developer


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = [
            "id",
            "name",
            "age", 
            "state", 
            "favorite_language", 
            "experience", 
        ]

    def create(self, validated_data: dict):
        return Developer.objects.create(**validated_data)
