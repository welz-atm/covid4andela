from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=12, null=True, blank=True)
    avgAge = models.DecimalField(max_digits=4, decimal_places=2)
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
    data = models.ForeignKey(Data, on_delete=models.CASCADE)

    def calculate_period(x):
        if x == 'weeks':
            return x * 7
        elif x == 'month':
            return x * 30
        else:
            return x


def currently_infected(self):
    cases = data.reportedCases * 10
    return cases


def infectionbyrequestedattime(self):
    factor = calculate_period(self.timeToElapse) // 3
    return self.currentlyInfected * 2 ** factor


def severe_case_by_requested_time(self):
    severe_case_per_time = self.infectionByRequestedAtTime * 0.15
    return severe_case_per_time


def hospital_beds_per_requested_time(self):
    hospital_bed_per_time = (self.data.totalHospitalBeds * 0.35) - self.severeCaseByRequestedTime
    return hospital_bed_per_time


def cases_for_icu_by_requested_time(self):
    case_icu_per_time = self.infectionByRequestedAtTime * 0.05
    return case_icu_per_time


def cases_for_ventilators_by_requested_time(self):
    case_ventilator_per_time = self.infectionByRequestedAtTime * 0.02
    return case_ventilator_per_time


def dollars_in_flight(self):
    dollars_in_flight = (self.self.infectionByRequestedAtTime * 0.65) * self.data.avgDailyIncome * 30
    return dollars_in_flight


class SevereImpact(models.Model):
    currentlyInfected = models.IntegerField(null=True, blank=True)
    infectionByRequestedAtTime = models.IntegerField(null=True, blank=True)
    severeCaseByRequestedTime = models.IntegerField(null=True, blank=True)
    hospitalBedsPerRequestedTime = models.IntegerField(null=True, blank=True)
    casesForIcuByRequestedTime = models.IntegerField(null=True, blank=True)
    casesForVentilatorsByRequestedTime = models.IntegerField(null=True, blank=True)
    dollarsInFlight = models.IntegerField(null=True, blank=True)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)

    def calculate_period(x):
        if x == 'weeks':
            return x * 7
        elif x == 'month':
            return x * 30
        else:
            return x

    def currently_infected(self):
        cases = data.reportedCases * 50
        return cases

    def infectionbyrequestedattime(self):
        factor = calculate_period(self.timeToElapse) // 3
        return self.currentlyInfected * 2 ** factor

    def severe_case_by_requested_time(self):
        severe_case_per_time = self.infectionByRequestedAtTime * 0.15
        return severe_case_per_time

    def hospital_beds_per_requested_time(self):
        hospital_bed_per_time = (self.data.totalHospitalBeds * 0.35) - self.severeCaseByRequestedTime
        return hospital_bed_per_time

    def cases_for_icu_by_requested_time(self):
        case_icu_per_time = self.infectionByRequestedAtTime * 0.05
        return case_icu_per_time

    def cases_for_ventilators_by_requested_time(self):
        case_ventilator_per_time = self.infectionByRequestedAtTime * 0.02
        return case_ventilator_per_time

    def dollars_in_flight(self):
        dollars_in_flight = (self.self.infectionByRequestedAtTime * 0.65) * self.data.avgDailyIncome * 30
        return dollars_in_flight