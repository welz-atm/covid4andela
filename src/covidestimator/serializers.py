from rest_framework import serializers
from .models import Data
from silk.models import Request


class DataFormSerializer(serializers.ModelSerializer):
    name = serializers.JSONField()
    avgAge = serializers.JSONField()
    avgDailyIncome = serializers.JSONField()
    avgDailyIncomePopulation = serializers.JSONField()
    periodType = serializers.JSONField()
    timeToElapse = serializers.JSONField()
    reportedCases = serializers.JSONField()
    population = serializers.JSONField()
    totalHospitalBeds = serializers.JSONField()

    class Meta:
        model = Data
        fields = ('name', 'avgAge', 'avgDailyIncome', 'avgDailyIncomePopulation', 'periodType', 'timeToElapse', 'reportedCases',
                  'population', 'totalHospitalBeds',)
				  

class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ('start_time','path','time_taken',)
