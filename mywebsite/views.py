from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):

    return HttpResponse("welcome")

def user_list(request):

    return render(request, 'vue第四天-2.html')

def tpl(request):
    name="sensmd"
    roles = ["ceo"]
    user_info = {"name": "sensmd", "salary": 100000, "role": "CTO"}

    return render(request, 'tpl.html', {"n1": name, "n2": roles, "n3": user_info})