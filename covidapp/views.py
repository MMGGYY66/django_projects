from django.shortcuts import render
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "9ded418773mshb7add42b953ffcap17120ejsn63e01fb3cfef",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()

# print(response.text)

# Create your views here.


def covidInfoView(request):
    num_of_results = int(response['results'])
    countries = []
    for result in range(0, num_of_results):
        country = (response['response'][result]['country'])
        countries.append(country)
    countries.sort()
    context = {'countries': countries, }
    if request.method == "POST":
        selectedCountry = request.POST['selectedCountry']

        for x in range(0, num_of_results):
            if selectedCountry == response['response'][x]['country']:
                day = response['response'][x]['day']
                newCases = response['response'][x]['cases']['new']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                active = response['response'][x]['cases']['active']
                total = response['response'][x]['cases']['total']
                death_cases = int(total) - (int(active) + int(recovered))
        context = {'selectedCountry': selectedCountry, 'day': day, 'countries': countries, 'newCases': newCases, 'critical': critical,'recovered': recovered, 'active': active, 'total': total, 'death_cases': death_cases, }
        return render(request, 'covidInfo.html', context)

    return render(request, 'covidInfo.html', context)
