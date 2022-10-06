from rest_framework import serializers
from api.models import VPS


class VPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPS
        fields = '__all__'


class VPSChangeStatusSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    class Meta:
        model = VPS
        fields = ['status']
