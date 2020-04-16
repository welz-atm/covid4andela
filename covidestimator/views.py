from silk.models import Request
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework_xml.renderers import XMLRenderer
from .serializers import DataFormSerializer,LogSerializer
from .estimator import currentlyinfected, currently_infected, infectionbyrequestedattime, \
    severecasesbyrequestedtime, hospitalbedsperrequestedtime, casesforicubyrequestedtime, \
    casesforventilatorsbyrequestedtime,dollarsinflight


@api_view(['POST','GET'])
def create_data(request):

    account_data = {}
    impact = {}
    severeimpact = {}
    serializer = DataFormSerializer(data=request.data)
    if serializer.is_valid():
        account = serializer.save()
        account_data['name'] = account.name
        account_data['avgAge']= account.avgAge
        account_data['avgDailyIncome'] = account.avgDailyIncome
        account_data['avgDailyIncomePopulation ']= account.avgDailyIncomePopulation
        account_data['periodType'] = account.periodType
        account_data['timeToElapse'] = account.timeToElapse
        account_data['reportedCases'] = account.reportedCases
        account_data['population'] = account.population
        account_data['totalHospitalBeds'] = account.totalHospitalBeds

        impact['currentlyInfected']= currentlyinfected(account.reportedCases)
        impact['infectionByRequestedAtTime'] = infectionbyrequestedattime(account.timeToElapse,currentlyinfected
        (account.reportedCases))
        impact['severeCaseByRequestedTim'] = severecasesbyrequestedtime(infectionbyrequestedattime
                                                                        (account.timeToElapse,currentlyinfected
                                                                        (account.reportedCases)))
        impact['hospitalBedsPerRequestedTime'] = hospitalbedsperrequestedtime(account.totalHospitalBeds,
                                                                              severecasesbyrequestedtime
                                                                              (infectionbyrequestedattime
                                                                               (account.timeToElapse,currentlyinfected
                                                                               (account.reportedCases))))
        impact['casesForIcuByRequestedTime'] = casesforicubyrequestedtime(infectionbyrequestedattime
                                                                          (account.timeToElapse,currentlyinfected
                                                                          (account.reportedCases)))
        impact['casesForVentilatorsByRequestedTime'] = casesforventilatorsbyrequestedtime(currentlyinfected
                                                                                          (account.reportedCases))
        impact['dollarsInFlight'] = dollarsinflight(currentlyinfected(account.reportedCases),account.avgDailyIncome)

        severeimpact['currentlyInfected'] = currently_infected(account.reportedCases)
        severeimpact['infectionByRequestedAtTime'] = infectionbyrequestedattime(account.timeToElapse,
                                                                          currently_infected(account.reportedCases))
        severeimpact['severeCaseByRequestedTim'] = severecasesbyrequestedtime(
            infectionbyrequestedattime(account.timeToElapse, currently_infected(account.reportedCases)))
        severeimpact['hospitalBedsPerRequestedTime'] = hospitalbedsperrequestedtime(account.totalHospitalBeds,
                                                                              severecasesbyrequestedtime(
                                                                                  infectionbyrequestedattime(
                                                                                      account.timeToElapse,
                                                                                      currently_infected(
                                                                                          account.reportedCases))))
        severeimpact['casesForIcuByRequestedTime'] = casesforicubyrequestedtime(
            infectionbyrequestedattime(account.timeToElapse, currently_infected(account.reportedCases)))
        severeimpact['casesForVentilatorsByRequestedTime'] = casesforventilatorsbyrequestedtime(
            currently_infected(account.reportedCases))
        severeimpact['dollarsInFlight'] = dollarsinflight(currently_infected(account.reportedCases),
                                                          account.avgDailyIncome)
        data = {
            'data':account_data,
            'impact':impact,
            'severeimpact':severeimpact
        }
        json = JSONRenderer().render(data)
        return Response(json)
    else:
        return Response(serializer.errors)


@api_view(['POST','GET'])
def create_data_xml(request):

    account_data = {}
    impact = {}
    severeimpact = {}
    serializer = DataFormSerializer(data=request.data)
    if serializer.is_valid():
        account = serializer.save()
        account_data['name'] = account.name
        account_data['avgAge']= account.avgAge
        account_data['avgDailyIncome'] = account.avgDailyIncome
        account_data['avgDailyIncomePopulation ']= account.avgDailyIncomePopulation
        account_data['periodType'] = account.periodType
        account_data['timeToElapse'] = account.timeToElapse
        account_data['reportedCases'] = account.reportedCases
        account_data['population'] = account.population
        account_data['totalHospitalBeds'] = account.totalHospitalBeds

        impact['currentlyInfected']= currentlyinfected(account.reportedCases)
        impact['infectionByRequestedAtTime'] = infectionbyrequestedattime(account.timeToElapse,currentlyinfected
        (account.reportedCases))
        impact['severeCaseByRequestedTim'] = severecasesbyrequestedtime(infectionbyrequestedattime
                                                                        (account.timeToElapse,currentlyinfected
                                                                        (account.reportedCases)))
        impact['hospitalBedsPerRequestedTime'] = hospitalbedsperrequestedtime(account.totalHospitalBeds,
                                                                              severecasesbyrequestedtime
                                                                              (infectionbyrequestedattime
                                                                               (account.timeToElapse,
                                                                                currentlyinfected
                                                                                (account.reportedCases))))
        impact['casesForIcuByRequestedTime'] = casesforicubyrequestedtime(infectionbyrequestedattime
                                                                          (account.timeToElapse,
                                                                           currentlyinfected(account.reportedCases)))
        impact['casesForVentilatorsByRequestedTime'] = casesforventilatorsbyrequestedtime(currentlyinfected
                                                                                          (account.reportedCases))
        impact['dollarsInFlight'] = dollarsinflight(currentlyinfected(account.reportedCases),account.avgDailyIncome)

        severeimpact['currentlyInfected'] = currently_infected(account.reportedCases)
        severeimpact['infectionByRequestedAtTime'] = infectionbyrequestedattime(account.timeToElapse,
                                                                          currently_infected(account.reportedCases))
        severeimpact['severeCaseByRequestedTim'] = severecasesbyrequestedtime(
            infectionbyrequestedattime(account.timeToElapse, currently_infected(account.reportedCases)))
        severeimpact['hospitalBedsPerRequestedTime'] = hospitalbedsperrequestedtime(account.totalHospitalBeds,
                                                                              severecasesbyrequestedtime(
                                                                                  infectionbyrequestedattime(
                                                                                      account.timeToElapse,
                                                                                      currently_infected(
                                                                                          account.reportedCases))))
        severeimpact['casesForIcuByRequestedTime'] = casesforicubyrequestedtime(
            infectionbyrequestedattime(account.timeToElapse, currently_infected(account.reportedCases)))
        severeimpact['casesForVentilatorsByRequestedTime'] = casesforventilatorsbyrequestedtime(
            currently_infected(account.reportedCases))
        severeimpact['dollarsInFlight'] = dollarsinflight(currently_infected(account.reportedCases),
                                                          account.avgDailyIncome)
        data = {
            'data':account_data,
            'impact':impact,
            'severeimpact':severeimpact
        }
        xml = XMLRenderer().render(data).format('.xml')
        return Response(xml)
    else:
        return Response(serializer.errors)


@api_view(['GET',])
def log_request(request):
    log = Request.objects.all()
    serializer = LogSerializer(log,many=True)
    return Response(serializer.data)
