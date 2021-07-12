from rest_framework import serializers
from .models import Result
# from .models import input_data

# class InputSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = input_data
#         # fields = ('userkey', 'videoNo', 'videobyte')
#         fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'