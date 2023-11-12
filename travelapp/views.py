from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import team

# Create your views here.
def demo(request):
     obj=place.objects.all()
     result=team.objects.all()
     return render(request, "index.html", {'result':result,'obj':obj})


def about(request):
     return render(request,"about.html")




# def addition(request):
#      x=int(request.GET['num1'])
#      y=int(request.GET['num2'])
#      res=x+y
#      return render(request,"result.html",{'result':res})
# def subtraction(request):
#      x = int(request.GET['num1'])
#      y = int(request.GET['num2'])
#      res1=x-y
#      return render(request,"result.html",{'result1':res1})
# def multiplication(request):
#      x = int(request.GET['num1'])
#      y = int(request.GET['num2'])
#      res2 = x ** y
#      return render(request,"result.html",{'result2':res2})
# def division(request):
#      x = int(request.GET['num1'])
#      y = int(request.GET['num2'])
#      res3 = x / y
#      return render(request, "result.html", {'result3': res3})
# def operation(request):
#      return render(request,"result.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})

# def about(request):
#      return render(request,"about.html")
# def contact(request):
#      return HttpResponse("AM CONTACT")