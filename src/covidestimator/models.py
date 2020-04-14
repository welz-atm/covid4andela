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

    @staticmethod
    def calculate_period(x):
        if x == 'weeks':
            return x * 7
        elif x == 'month':
            return x * 30
        else:
            return x

    @staticmethod
    def currentlyinfected(x):
        return x * 10

    @staticmethod
    def infectionbyrequestedattime(x, y):
        factor = Impact.calculate_period(x) // 3
        return Impact.currentlyinfected(y) * 2 ** factor

    @staticmethod
    def severecasesbyrequestedtime(x):
        return x * 0.15

    @staticmethod
    def hospitalbedsperrequestedtime(x, y):
        return (x * 0.35) - y

    @staticmethod
    def casesforicubyrequestedtime(x):
        return x * 0.05

    @staticmethod
    def casesforventilatorsbyrequestedtime(x):
        return x * 0.02

    @staticmethod
    def dollarsinflight(x, y):
        return (x * 0.65) * y * 30


class SevereImpact(models.Model):
    currentlyInfected = models.FloatField(null=True, blank=True)
    infectionByRequestedAtTime = models.FloatField(null=True, blank=True)
    severeCaseByRequestedTime = models.FloatField(null=True, blank=True)
    hospitalBedsPerRequestedTime = models.FloatField(null=True, blank=True)
    casesForIcuByRequestedTime = models.FloatField(null=True, blank=True)
    casesForVentilatorsByRequestedTime = models.FloatField(null=True, blank=True)
    dollarsInFlight = models.IntegerField(null=True, blank=True)
    data = models.ForeignKey(Data,on_delete=models.CASCADE)

    @staticmethod
    def calculate_period(x):
        if x == 'weeks':
            return x * 7
        elif x == 'month':
            return x * 30
        else:
            return x

    @staticmethod
    def currentlyinfected(x):
        return x * 10

    @staticmethod
    def infectionbyrequestedattime(x, y):
        factor = SevereImpact.calculate_period(x) // 3
        return SevereImpact.currentlyinfected(y) * 2 ** factor

    @staticmethod
    def severecasesbyrequestedtime(x):
        return x * 0.15

    @staticmethod
    def hospitalbedsperrequestedtime(x, y):
        return (x * 0.35) - y

    @staticmethod
    def casesforicubyrequestedtime(x):
        return x * 0.05

    @staticmethod
    def casesforventilatorsbyrequestedtime(x):
        return x * 0.02

    @staticmethod
    def dollarsinflight(x, y):
        return (x * 0.65) * y * 30