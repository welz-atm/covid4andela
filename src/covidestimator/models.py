from django.db import models
from django.db.models.signals import post_save,post_init
from django.dispatch import receiver
from datetime import timedelta


class Data(models.Model):
    name = models.CharField(max_length=12, null=True, blank=True)
    avgAge = models.DecimalField(max_digits=4,decimal_places=2)
    avgDailyIncome = models.IntegerField(null=True, blank=True)
    avgDailyIncomePopulation = models.FloatField(null=True, blank=True)
    periodType = models.CharField(max_length=12, null=True, blank=True)
    timeToElapse = models.IntegerField(null=True, blank=True)
    reportedCases = models.IntegerField(null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)
    totalHospitalBeds = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Impact(models.Model):
    currentlyInfected = models.IntegerField(null=True, blank=True)
    infectionByRequestedAtTime = models.IntegerField(null=True, blank=True)
    severeCaseByRequestedTime = models.IntegerField(null=True, blank=True)
    hospitalBedsPerRequestedTime = models.IntegerField(null=True, blank=True)
    casesForIcuByRequestedTime = models.IntegerField(null=True, blank=True)
    casesForVentilatorsByRequestedTime = models.IntegerField(null=True, blank=True)
    dollarsInFlight = models.IntegerField(null=True, blank=True)
    data = models.ForeignKey(Data,on_delete=models.CASCADE)

    def calculate_period(self):
        if self.data.periodType == 'weeks':
            return self.data.periodType * 7
        elif self.data.periodType == 'month':
            return self.data.periodType * 30
        else:
            return self.data.periodType

    def currentlyinfected(self):
        return self.data.reportedCases * 10

    def infectionbyrequestedattime(self):
        factor = self.data.timeToElapse.calculate_period() / 3
        return self.data.reportedCases.currently_infected() * 2**factor

    def severecasesbyrequestedtime(self):
        return self.infectionByRequestedAtTime() * 0.15

    def hospitalbedsperrequestedtime(self):
        return (self.data.totalHospitalBeds * 0.35) - self.severeCaseByRequestedTime

    def cases_for_icu_by_requested_time(self):
        return self.infectionByRequestedAtTime()* 0.05

    def cases_for_ventilators_by_requested_time(self):
        return self.infectionByRequestedAtTime() * 0.02

    def dollars_in_flight(self):
        return (self.infectedByRequestedAtTime()*0.65)*self.avgDailyIncome*30


class SevereImpact(models.Model):
    currentlyInfected = models.FloatField(null=True, blank=True)
    infectionByRequestedAtTime = models.FloatField(null=True, blank=True)
    severeCaseByRequestedTime = models.FloatField(null=True, blank=True)
    hospitalBedsPerRequestedTime = models.FloatField(null=True, blank=True)
    casesForIcuByRequestedTime = models.FloatField(null=True, blank=True)
    casesForVentilatorsByRequestedTime = models.FloatField(null=True, blank=True)
    dollarsInFlight = models.IntegerField(null=True, blank=True)
    data = models.ForeignKey(Data,on_delete=models.CASCADE)

    def currently_infected(self):
        return self.data.reportedCases * 10

    def infectionbyrequestedattime(self):
        factor = self.data.timeToElapse / 3
        return self.data.reportedCases.currently_infected() * 2 ** factor

    def severecasesbyrequestedtime(self):
        return self.infectionByRequestedAtTime() * 0.15

    def hospitalbedsperrequestedtime(self):
        return (self.data.totalHospitalBeds * 0.35) - self.severeCaseByRequestedTime

    def cases_for_icu_by_requested_time(self):
        return self.infectionByRequestedAtTime() * 0.05

    def cases_for_ventilators_by_requested_time(self):
        return self.infectionByRequestedAtTime() * 0.02

    def dollars_in_flight(self):
        return (self.infectedByRequestedAtTime() * 0.65) * self.avgDailyIncome * 30


class logs(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    path = models.URLField()
    time = models.IntegerField