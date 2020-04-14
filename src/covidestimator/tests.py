import pytest
from .models import Data,Impact,SevereImpact
from django.urls import reverse


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
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  currentlyInfected = Impact.currentlyinfected(data.reportedCases)
  assert currentlyInfected == 5650
  
@pytest.mark.django_db
def test_infection_by_requested_at_time():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  infectionByRequestedAtTime = Impact.infectionbyrequestedattime(data.timeToElapse, Impact.currentlyinfected(data.reportedCases))
  assert infectionByRequestedAtTime == 29622272000
  
 @pytest.mark.django_db
def test_severe_cases_by_requested_time():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  severeCasesByRequestedTime = Impact.severecasesbyrequestedtime(Impact.infectionbyrequestedattime(data.timeToElapse, Impact.currentlyinfected(data.reportedCases)))
  assert severeCasesByRequestedTime == 4443340800.0
  
@pytest.mark.django_db
def test_hospital_beds_per_requested_time():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  hospitalBedsPerRequestedTime = Impact.hospitalbedsperrequestedtime(data.totalHospitalBeds, Impact.severecasesbyrequestedtime(
                   Impact.infectionbyrequestedattime(data.timeToElapse, Impact.currentlyinfected(data.reportedCases))))
  assert hospitalBedsPerRequestedTime ==  -4441976827.95
  
@pytest.mark.django_db
def test_cases_for_icu_by_requested_time():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  casesForIcuByRequestedTime = Impact.hospitalbedsperrequestedtime(data.totalHospitalBeds, Impact.severecasesbyrequestedtime(
                   Impact.infectionbyrequestedattime(data.timeToElapse, Impact.currentlyinfected(data.reportedCases))))
  assert casesForIcuByRequestedTime == 1481113600.0
  
 @pytest.mark.django_db
def test_cases_for_ventilators_by_requested_time():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  casesForCentilatorsByRequestedTime = Impact.casesforventilatorsbyrequestedtime(Impact.infectionbyrequestedattime(data.timeToElapse, Impact.currentlyinfected(data.reportedCases)))
  assert casesForCentilatorsByRequestedTime == 113.0
  
@pytest.mark.django_db
def test_dollars_in_flight():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  dollarsInFlight  = Impact.infectedByRequestedAtTime()*0.65)*data.avgDailyIncome*30
  assert dollarsInFlight  == 1322100.0


#SevereImpact
   
  
@pytest.mark.django_db
def test_severe_currently_infected():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  currentlyInfected = SevereImpact.currentlyinfected(data.reportedCases)
  assert currentlyInfected == 28250
  
@pytest.mark.django_db
def test_severe_infection_by_requested_at_time():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  infectionByRequestedAtTime = SevereImpact.infectionbyrequestedattime(data.timeToElapse, SevereImpact.currentlyinfected(data.reportedCases))
  assert infectionByRequestedAtTime == 148111360000
  
 @pytest.mark.django_db
def test_severe_severe_cases_by_requested_time():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  severeCasesByRequestedTime = SevereImpact.severecasesbyrequestedtime(SevereImpact.infectionbyrequestedattime(data.timeToElapse, SevereImpact.currentlyinfected(data.reportedCases)))
  assert severeCasesByRequestedTime == 22216704000.0
  
@pytest.mark.django_db
def test_severe_hospital_beds_per_requested_time():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  hospitalBedsPerRequestedTime  = SevereImpact.hospitalbedsperrequestedtime(data.totalHospitalBeds, SevereImpact.severecasesbyrequestedtime(
                   SevereImpact.infectionbyrequestedattime(data.timeToElapse, SevereImpact.currentlyinfected(data.reportedCases))))
  assert hospitalBedsPerRequestedTime == -22215340027.95
  
@pytest.mark.django_db
def test_severe_cases_for_icu_by_requested_time():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  casesForIcuByRequestedTime = SevereImpact.hospitalbedsperrequestedtime(data.totalHospitalBeds, SevereImpact.severecasesbyrequestedtime(
                   SevereImpact.infectionbyrequestedattime(data.timeToElapse, SevereImpact.currentlyinfected(data.reportedCases))))
  assert casesForIcuByRequestedTime == 7405568000.0
  
 @pytest.mark.django_db
def test_severe_cases_for_ventilators_by_requested_time():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  casesForCentilatorsByRequestedTime = SevereImpact.casesforventilatorsbyrequestedtime(SevereImpact.infectionbyrequestedattime(data.timeToElapse, SevereImpact.currentlyinfected(data.reportedCases)))
  assert casesForCentilatorsByRequestedTime == 565.0
  
@pytest.mark.django_db
def test_severe_dollars_in_flight():
  data = Data.objects.create(name= "Jamaica",avgAge=26.5,avgDailyIncome=12,avgDailyIncomePopulation=3,periodType="days",timeToElapse=58,reportedCases=565,population=12000987,totalHospitalBeds=3897063)
  dollarsInFlight  = SevereImpact.infectedByRequestedAtTime()*0.65)*data.avgDailyIncome*30
  assert dollarsInFlight  == 6610500.0
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  Impact.casesforicubyrequestedtime(Impact.infectionbyrequestedattime(data.timeToElapse, Impact.currentlyinfected(data.reportedCases)))