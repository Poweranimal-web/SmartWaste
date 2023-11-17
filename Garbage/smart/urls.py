from django.urls import path

from smart.views import MyView

urlpatterns = [
    path("", MyView.as_view()),

]