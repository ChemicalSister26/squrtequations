
from django.contrib import admin
from django.urls import path

from views import AnswerAPIView, EnterYourNumbers, main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', EnterYourNumbers, name='index'),
    path('API/numberlist', AnswerAPIView.as_view()),
    path('main/', main, name='main'),
]
