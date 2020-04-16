from django.contrib import admin
from .models import Impact,SevereImpact,Data
from silk.models import Request


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


class RequestAdmin(admin.ModelAdmin):
    list_display = ('start_time','path','time_taken',)


admin.site.register(Data,DataAdmin)
admin.site.register(Request,RequestAdmin)
admin.site.register(Impact,ImpactAdmin)
admin.site.register(SevereImpact,SevereImpactAdmin)
