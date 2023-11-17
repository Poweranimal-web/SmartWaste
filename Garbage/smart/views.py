import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from smart.models import User
class RegView(View):
    def get(self, request):
        return render(request, "reg.html")
    def post(self, request):
        data = request.body
        data = json.loads(data)
        if data["status"] == "create":
            exist_email = User.objects.filter(email=data["email"]).exists()
            if exist_email:
                return JsonResponse({"status": "account exist"})
            else:
                User.objects.create(nickname=data["nickname"], email=data["email"], password=data["password"])
                request.session["Email"] = data["email"]
                request.session["auth"] = True
                return JsonResponse({"status": "created"})
        if data["status"] == "validate":
            exist_email = User.objects.filter(email=data["email"], password=data["password"]).exists()
            if exist_email:
                request.session["Email"] = data["email"]
                request.session["auth"] = True
                return JsonResponse({"status": "checked"})
            else:
                return JsonResponse({"status": "not exist"})
class MainView(View):
    def get(self,request):
        return render(request, "base.html")