from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from rest_framework import generics

from squrteq.forms import EnterNumbersHere
from squrteq.models import *
# Create your views here.
from squrteq.serializers import AnswerSerializer


# def index(request):
#     return HttpResponse('hello everybody')


class AnswerAPIView(generics.ListCreateAPIView):
    queryset = Forsqrt.objects.all()
    serializer_class = AnswerSerializer

class EnterYourNumbers(FormView):

    form_class = EnterNumbersHere
    template_name = 'index.html'
    fields = '__all__'
    success_url = reverse_lazy('data')


