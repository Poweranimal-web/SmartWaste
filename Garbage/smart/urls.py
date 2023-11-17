from django.urls import path

from smart.views import RegView, MainView

urlpatterns = [
    path("reg/", RegView.as_view(), name="reg"),
    path("", MainView.as_view()),

]