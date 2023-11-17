from django.urls import path

from smart.views import RegView, MainView

urlpatterns = [
    path("reg/", RegView.as_view()),
    path("", MainView.as_view()),

]