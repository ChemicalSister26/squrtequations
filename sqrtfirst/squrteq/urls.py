
from django.contrib import admin
from django.urls import path

from views import AnswerAPIView, EnterYourNumbers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', EnterYourNumbers.as_view()),
    path('API/numberlist', AnswerAPIView.as_view())
]
