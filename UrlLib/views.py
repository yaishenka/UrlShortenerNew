from rest_framework import generics, mixins
from rest_framework.views import Response
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .serializers import UrlSerializer
from .models import Url


def goto(request, link):
    try:
        url = Url.objects.get(short_url=link)
    except Url.DoesNotExist:
        return HttpResponse("Unknown url!")

    link = url.full_url
    url.used += 1
    url.save()
    return redirect(link)


class UrlManagerView(generics.ListCreateAPIView):
    serializer_class = UrlSerializer

    def get_queryset(self):
        queryset = Url.objects.filter(creator=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class UrlDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UrlSerializer
    lookup_url_kwarg = 'short_url'

    def get_queryset(self):
        queryset = Url.objects.filter(creator=self.request.user)
        return queryset

    def get_object(self):
        short_url = self.kwargs[self.lookup_url_kwarg]
        return get_object_or_404(Url, short_url=short_url)