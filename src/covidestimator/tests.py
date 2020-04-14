import pytest
from .models import Data
from django.urls import reverse
from .estimator import currentlyinfected, currently_infected, infectionbyrequestedattime, \
    severecasesbyrequestedtime, hospitalbedsperrequestedtime, casesforicubyrequestedtime, \
    casesforventilatorsbyrequestedtime,dollarsinflight


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_log_view(api_client):
    url = reverse('impact_logs')
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_json_view(api_client):
    url = reverse('impact_json')
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_xml_view(api_client):
    url = reverse('impact_xml')
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_default_view(api_client):
    url = reverse('impact_default')
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_currently_infected():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    currently_infected = currentlyinfected(data.reportedCases)
    assert currently_infected == 5650


@pytest.mark.django_db
def test_infection_by_requested_at_time():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    infection_byrequestedat_time = infectionbyrequestedattime(data.timeToElapse,currentlyinfected(data.reportedCases))
    assert infection_byrequestedat_time == 29622272000


@pytest.mark.django_db
def test_severe_cases_by_requested_time():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    severecases_byrequestedtime = severecasesbyrequestedtime(infectionbyrequestedattime(data.timeToElapse,
                                                                                        currentlyinfected
                                                                                        (data.reportedCases)))
    assert severecases_byrequestedtime == 4443340800.0


@pytest.mark.django_db
def test_hospital_beds_per_requested_time():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    hospitalbedsperrequested_time = hospitalbedsperrequestedtime(data.totalHospitalBeds,severecasesbyrequestedtime
    (infectionbyrequestedattime(data.timeToElapse,currentlyinfected(data.reportedCases))))
    assert hospitalbedsperrequested_time == -4441976827.95


@pytest.mark.django_db
def test_cases_for_icu_by_requested_time():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    casesforicubyrequested_time = casesforicubyrequestedtime(infectionbyrequestedattime(data.timeToElapse,
                                                                                        currentlyinfected
                                                                                        (data.reportedCases)))
    assert casesforicubyrequested_time == 1481113600.0


@pytest.mark.django_db
def test_cases_for_ventilators_by_requested_time():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    casesforventilatorsbyrequested_time = casesforventilatorsbyrequestedtime(currentlyinfected(data.reportedCases))
    assert casesforventilatorsbyrequested_time == 113.0


@pytest.mark.django_db
def test_dollars_in_flight():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    dollarsin_flight = dollarsinflight(currentlyinfected(data.reportedCases),data.avgDailyIncome)
    assert dollarsin_flight == 1322100.0

# SevereImpact


@pytest.mark.django_db
def test_currently_infected():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    currentlyinfected = currently_infected(data.reportedCases)
    assert currentlyinfected == 28250


@pytest.mark.django_db
def test_infection_by_requested_at_time():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    infection_byrequestedat_time = infectionbyrequestedattime(data.timeToElapse,currently_infected(data.reportedCases))
    assert infection_byrequestedat_time == 148111360000


@pytest.mark.django_db
def test_severe_cases_by_requested_time():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    severecases_byrequestedtime = severecasesbyrequestedtime(infectionbyrequestedattime(data.timeToElapse,
                                                                                        currently_infected
                                                                                        (data.reportedCases)))
    assert severecases_byrequestedtime == 22216704000.0


@pytest.mark.django_db
def test_hospital_beds_per_requested_time():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    hospitalbedsperrequested_time = hospitalbedsperrequestedtime(data.totalHospitalBeds,severecasesbyrequestedtime(
                                    infectionbyrequestedattime(data.timeToElapse,currently_infected(data.reportedCases))
                                                                                             )
                                                                 )
    assert hospitalbedsperrequested_time == -22215340027.95


@pytest.mark.django_db
def test_cases_for_icu_by_requested_time():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    casesforicubyrequested_time = casesforicubyrequestedtime(infectionbyrequestedattime(data.timeToElapse,
                                                                                        currently_infected
                                                                                        (data.reportedCases)))
    assert casesforicubyrequested_time == 7405568000.0


@pytest.mark.django_db
def test_cases_for_ventilators_by_requested_time():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    casesforventilatorsbyrequested_time = casesforventilatorsbyrequestedtime(currently_infected(data.reportedCases))
    assert casesforventilatorsbyrequested_time == 565.0


@pytest.mark.django_db
def test_dollars_in_flight():
    data = Data.objects.create_user(name="Jamaica", avgAge=26.5, avgDailyIncome=12, avgDailyIncomePopulation=3,
                                    periodType="days", timeToElapse=58, reportedCases=565, population=12000987,
                                    totalHospitalBeds=3897063)
    dollarsin_flight = dollarsinflight(currently_infected(data.reportedCases),data.avgDailyIncome)
    assert dollarsin_flight == 6610500.0