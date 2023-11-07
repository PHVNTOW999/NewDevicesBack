from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from .serializer import *


class PhoneView(generics.UpdateAPIView):
    @staticmethod
    def post(request, *args, **kwargs):
        queryset = Phone.objects.create()

        if request.data['num']:
            queryset.num = request.data['num']

        if request.data['desc']:
            queryset.desc = request.data['desc']

        queryset.save()

        return HttpResponse(queryset.uuid)

    def delete(self, request, *args, **kwargs):
        queryset = Phone.objects.get(uuid=self.kwargs['uuid']).delete()

        return JsonResponse(queryset, safe=False)


class ClientsListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Client.objects.all().order_by('-created').values()
        serializer_class = ClientSerializer(queryset, many=True)

        return JsonResponse(serializer_class.data, safe=False)


# Meets
class MeetsViewList(generics.ListAPIView):
    queryset = Meet.objects.all().order_by('-created')
    serializer_class = MeetSerializer

    @staticmethod
    def post(request, *args, **kwargs):
        queryset = Meet.objects.create()

        if request.data['isActive']:
            queryset.isActive = request.data['isActive']

        if request.data['no']:
            queryset.no = request.data['no']

        if request.data['phone']:
            queryset.phone = request.data['phone']

        if request.data['datetime']:
            queryset.datetime = request.data['datetime']

        if request.data['details']:
            queryset.details = request.data['details']

        queryset.save()

        return HttpResponse(queryset)


class MeetView(generics.UpdateAPIView):

    def put(self, request, *args, **kwargs):
        queryset = Meet.objects.get(uuid=self.kwargs['uuid'])
        serializer = MeetSerializer(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data)
        return HttpResponse(serializer.data)

    def patch(self, request, *args, **kwargs):
        queryset = Meet.objects.get(uuid=self.kwargs['uuid'])

        if request.data['client'] is not '':
            new_client_uuid = request.data['client']
            new_client = Client.objects.get(uuid=new_client_uuid['uuid'])
            queryset.client = new_client

        if request.data['phones'] is not '':
            new_phone = Phone.objects.get(uuid=request.data['phones'])
            queryset.phones.add(new_phone)

        if request.data['emails'] is not '':
            new_email = Email.objects.get(uuid=request.data['emails'])
            queryset.emails.add(new_email)

        queryset.save()
        serializer_class = MeetSerializer(queryset)

        return HttpResponse(serializer_class.data)

    def delete(self, request, *args, **kwargs):
        queryset = Meet.objects.get(uuid=self.kwargs['uuid']).delete()

        return JsonResponse(queryset, safe=False)
