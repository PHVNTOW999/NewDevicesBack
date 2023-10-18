from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from .serializer import *


class MeetsViewList(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Meet.objects.all().order_by('-created').values()
        serializer_class = MeetSerializer(queryset, many=True)

        return JsonResponse(serializer_class.data, safe=False)

    @staticmethod
    def post(request, *args, **kwargs):
        queryset = Meet.objects.create()

        if request.data['isActive']:
            queryset.isActive = request.data['isActive']

        if request.data['no']:
            queryset.no = request.data['no']

        if request.data['name']:
            queryset.name = request.data['name']

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

        if request.data['datetime'] is "":
            queryset.datetime = None
            queryset.save()
            return HttpResponse(queryset)

    def delete(self, request, *args, **kwargs):
        queryset = Meet.objects.get(uuid=self.kwargs['uuid']).delete()

        return JsonResponse(queryset, safe=False)
