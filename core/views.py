from django.shortcuts import render
from django.http import HttpResponse

from django.views import View

# Create your views here.
def index(self):
    return HttpResponse("Worker")

class HomePage(View):
    def get(self,request):
        
        return render(request,'index.html',{})