from django.test import TestCase, Client
from django.urls import reverse
from .models import Data,Impact,SevereImpact


class TestData(TestCase):
    def setUp(self):
        self.data = Data.objects.create_user(name='Welz Inc', first_name='Ay', last_name='Shols',
                                             email='w@nomugu.com', address='1,Abiona Ikorodu',
                                             state='Lagos', country='Nigeria', telephone='08167847286',
                                             password='test123', is_merchant=True)


class TestAddProduct(TestData, TestCase):
    def test_new_data(self):
        data = Data.objects.get(name='Laptop')
        self.assertEqual(data.name, 'Africa')


class TestDataViews(TestData, TestCase):
    def test_json_view(self):
        url = reverse('impact_json')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_xml_view(self):
        url = reverse('impact_xml')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_default_view(self):
        url = reverse('impact_default')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_logs_view(self):
        url = reverse('impact_logs')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)


class TestAddCategory(TestData, TestCase):
    def test_impact_currently_infected(self):
        data = Data.objects.get(name='Africa')
        response = Impact.currentlyinfected(data.reportedCases)
        self.assertEqual(response.currentlyInfected, 6870)

    def test_impact_infection_by_requested_at_time(self):
        data = Data.objects.get(name='Africa')
        response = Impact.infectionbyrequestedattime(data.timeToElapse, Impact.currentlyinfected(data.reportedCases))
        self.assertEqual(response.infectionByRequestedAtTime, 6870)

    def test_impact_severe_cases_by_requested_time(self):
        data = Data.objects.get(name='Africa')
        response = Impact.severecasesbyrequestedtime(
        Impact.infectionbyrequestedattime(data.timeToElapse, Impact.currentlyinfected(data.reportedCases)))
        self.assertEqual(response.severecasesbyrequestedtime, 6870)

    def test_impact_hospital_beds_per_requested_time(self):
        data = Data.objects.get(name='Africa')
        response = Impact.hospitalbedsperrequestedtime(data.totalHospitalBeds, Impact.severecasesbyrequestedtime(
        Impact.infectionbyrequestedattime(data.timeToElapse, Impact.currentlyinfected(data.reportedCases))))
        self.assertEqual(response.severecasesbyrequestedtime, 6870)

    def test_impact_cases_for_icu_by_requested_time(self):
        data = Data.objects.get(name='Africa')
        response = Impact.casesforicubyrequestedtime(
        Impact.infectionbyrequestedattime(data.timeToElapse, Impact.currentlyinfected(data.reportedCases)))
        self.assertEqual(response.casesforicubyrequestedtime, 6870)

    def test_impact_cases_for_ventilator_by_requested_time(self):
        data = Data.objects.get(name='Africa')
        response = Impact.casesforventilatorsbyrequestedtime(
        Impact.infectionbyrequestedattime(data.timeToElapse, Impact.currentlyinfected(data.reportedCases)))
        self.assertEqual(response.casesforicubyrequestedtime, 6870)


class TestSevereImpactEstimatorFunctions(TestCase, TestCase):

    def test_severe_impact_currently_infected(self):
        data = Data.objects.get(name='Africa')
        response = SevereImpact.currentlyinfected(data.reportedCases)
        self.assertEqual(response.currentlyInfected, 6870)

    def test_severe_impact_infection_by_requested_at_time(self):
        data = Data.objects.get(name='Africa')
        response = SevereImpact.infectionbyrequestedattime(data.timeToElapse,
                                                           SevereImpact.currentlyinfected(data.reportedCases))
        self.assertEqual(response.infectionByRequestedAtTime, 6870)

    def test_severe_impact_severe_cases_by_requested_time(self):
        data = Data.objects.get(name='Africa')
        response = SevereImpact.severecasesbyrequestedtime(SevereImpact.infectionbyrequestedattime(data.timeToElapse,
                                                            SevereImpact.currentlyinfected(data.reportedCases)))
        self.assertEqual(response.severeCaseByRequestedTim, 6870)

    def test_severe_impact_hospital_beds_per_requested_time(self):
        data = Data.objects.get(name='Africa')

        response = SevereImpact.hospitalbedsperrequestedtime(data.totalHospitalBeds,SevereImpact.severecasesbyrequestedtime(SevereImpact.infectionbyrequestedattime(data.timeToElapse,SevereImpact.currentlyinfected(data.reportedCases))))
        self.assertEqual(response.hospitalBedsPerRequestedTime, 6870)

    def test_severe_impact_cases_for_icu_by_requested_time(self):
        data = Data.objects.get(name='Africa')
        response = SevereImpact.casesforicubyrequestedtime(SevereImpact.infectionbyrequestedattime(data.timeToElapse, SevereImpact.currentlyinfected(data.reportedCases)))
        self.assertEqual(response.casesForIcuByRequestedTime, 6870)

    def test_severe_impact_cases_for_ventilator_by_requested_time(self):
        data = Data.objects.get(name='Africa')
        response = SevereImpact.casesforventilatorsbyrequestedtime(SevereImpact.infectionbyrequestedattime(data.timeToElapse, SevereImpact.currentlyinfected(data.reportedCases)))
        self.assertEqual(response.casesForVentilatorsByRequestedTime, 6870)

