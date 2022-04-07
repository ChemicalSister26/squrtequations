from rest_framework import serializers

from squrteq.models import Forsqrt


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forsqrt
        fields = ('first_number', 'second_number', 'third_number', 'res_1', 'res_2', 'unsolvable')

    def create(self, validated_data):
        return Forsqrt.objects.create(**validated_data)