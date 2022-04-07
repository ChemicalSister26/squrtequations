from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from squrteq.models import *
# Create your views here.
from squrteq.serializers import AnswerSerializer


def index(request):
    return HttpResponse('hello everybody')


class AnswerAPIView(generics.ListCreateAPIView):
    queryset = Forsqrt.objects.all()
    serializer_class = AnswerSerializer