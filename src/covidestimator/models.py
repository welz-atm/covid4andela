from django.db import models


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


class SevereImpact(models.Model):
    currentlyInfected = models.FloatField(null=True, blank=True)
    infectionByRequestedAtTime = models.FloatField(null=True, blank=True)
    severeCaseByRequestedTime = models.FloatField(null=True, blank=True)
    hospitalBedsPerRequestedTime = models.FloatField(null=True, blank=True)
    casesForIcuByRequestedTime = models.FloatField(null=True, blank=True)
    casesForVentilatorsByRequestedTime = models.FloatField(null=True, blank=True)
    dollarsInFlight = models.IntegerField(null=True, blank=True)
    data = models.ForeignKey(Data,on_delete=models.CASCADE)