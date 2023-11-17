from django.urls import path

from smart.views import RegView

urlpatterns = [
    path("reg/", RegView.as_view()),
    # path("", MainView.as_view()),

]