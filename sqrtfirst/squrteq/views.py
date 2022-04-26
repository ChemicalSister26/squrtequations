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

            return HttpResponseRedirect('/main')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = EnterNumbersHere()

    return render(request, 'index.html', {'form': form, 'form1': form1})





def main(request):
    return HttpResponse('this page')
