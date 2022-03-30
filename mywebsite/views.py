from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):

    return HttpResponse("welcome")

def user_list(request):

    return render(request, 'vue第四天-2.html')