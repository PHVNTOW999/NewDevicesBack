# import requests
# from bs4 import BeautifulSoup
# from django.http import JsonResponse
# from rest_framework import generics


# class Curr(generics.ListAPIView):
#     def get(request, *args, **kwargs):
#         amdLink = "https://freecurrencyrates.com/ru/convert-USD-AMD"
#
#         usdLink = "https://freecurrencyrates.com/ru/convert-AMD-USD"
#         eurLink = "https://freecurrencyrates.com/ru/convert-AMD-EUR"
#         rubLink = "https://freecurrencyrates.com/ru/convert-AMD-RUB"
#         cnyLink = "https://freecurrencyrates.com/ru/convert-AMD-CNY"
#
#         headers = {
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
#                           "Chrome/88.0.4324.182 Safari/537.36"}
#
#         amd = requests.get(amdLink, headers=headers).text
#
#         usd = requests.get(usdLink, headers=headers).text
#         eur = requests.get(eurLink, headers=headers).text
#         rub = requests.get(rubLink, headers=headers).text
#         cny = requests.get(cnyLink, headers=headers).text
#
#         amdSoup = BeautifulSoup(amd, 'lxml')
#
#         usdSoup = BeautifulSoup(usd, 'lxml')
#         eurSoup = BeautifulSoup(eur, 'lxml')
#         rubSoup = BeautifulSoup(rub, 'lxml')
#         cnySoup = BeautifulSoup(cny, 'lxml')
#
#         usdAMD = amdSoup.find('input', {"id": "value_to"})['value']
#
#         amdUSD = usdSoup.find('input', {"id": "value_to"})['value']
#         amdEUR = eurSoup.find('input', {"id": "value_to"})['value']
#         amdRUB = rubSoup.find('input', {"id": "value_to"})['value']
#         amdCNY = cnySoup.find('input', {"id": "value_to"})['value']
#
#         obj = {
#             "AMD": usdAMD,
#             'USD': (float(amdUSD) / 10),
#             'EUR': (float(amdEUR) / 10),
#             'RUB': amdRUB,
#             'CNY': amdCNY,
#         }
#
#         return JsonResponse(obj)