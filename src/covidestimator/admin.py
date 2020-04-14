from django.contrib import admin
from .models import Impact,SevereImpact,Data


class ImpactAdmin(admin.ModelAdmin):
    list_display = ('data','currentlyInfected','infectionByRequestedAtTime','severeCaseByRequestedTime',
                    'hospitalBedsPerRequestedTime','casesForIcuByRequestedTime',
                    'casesForVentilatorsByRequestedTime',)


class SevereImpactAdmin(admin.ModelAdmin):
    list_display = ('data','currentlyInfected','infectionByRequestedAtTime','severeCaseByRequestedTime',
                    'hospitalBedsPerRequestedTime','casesForIcuByRequestedTime',
                    'casesForVentilatorsByRequestedTime',)


class DataAdmin(admin.ModelAdmin):
    list_display = ('name','avgAge','avgDailyIncome','avgDailyIncomePopulation','periodType','timeToElapse',
                    'reportedCases','population','totalHospitalBeds',)


admin.site.register(Data,DataAdmin)
admin.site.register(Impact,ImpactAdmin)
admin.site.register(SevereImpact,SevereImpactAdmin)
