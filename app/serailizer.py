from rest_framework import serializers
from .models import overspeed

class OverspeedSerializer(serializers.ModelSerializer):
    class Meta:
        model= overspeed
        fields = "__all__"