from django.shortcuts import render
from .forms import employee_register_form
# Create your views here.

def employee_register(request):

    if request.method == "POST":
        a =  employee_register_form(request.POST)

        if a.is_valid():
            a.save()
            return render("/")
        
    a = employee_register_form()

    return render(request,'signup.html',{'a':a})
