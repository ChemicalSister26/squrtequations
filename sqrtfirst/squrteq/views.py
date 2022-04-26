from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from rest_framework import generics
from django.core import serializers
from squrteq.forms import EnterNumbersHere, Answers
from squrteq.models import *
# Create your views here.
from squrteq.serializers import AnswerSerializer
from squrteq.solvation import functionsqrt
import sqlite3

class AnswerAPIView(generics.ListCreateAPIView):
    queryset = Forsqrt.objects.all()
    serializer_class = AnswerSerializer

# class EnterYourNumbers(FormView):
#
#     form_class = EnterNumbersHere
#     template_name = 'index.html'
#     fields = '__all__'
#     success_url = reverse_lazy('data')

def EnterYourNumbers(request):
    form1 = Answers# if this is a POST request we need to process the form data
    x = 0
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EnterNumbersHere(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/index')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = EnterNumbersHere()
    q = Forsqrt.objects.all()
    q1 = q[len(q)-1].first_number
    q2 = q[len(q) - 1].second_number
    q3 = q[len(q) - 1].third_number
    x = functionsqrt(q[len(q)-1].first_number, q[len(q)-1].second_number, q[len(q)-1].third_number)


    return render(request, 'index.html', {'form': form, 'form1': form1, 'x': x, 'q1': q1, 'q2': q2, "q3": q3})





def main(request):
    return HttpResponse('this page')
