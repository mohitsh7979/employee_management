from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from farmer_app.forms import EmployeeForm
from dealer_app.forms import DealerForm, DistributerForm
from dealer_app.models import Dealer, Distributer
from app.models import CustomUser
from django.db.models import Q
from employee_app.models import Employee_model
from farmer_app.models import Farmer
from app.models import Resourse


@login_required(login_url='/')
def HOME(request):

    farmer_count = Farmer.objects.all().count()
    dealer_count = Dealer.objects.all().count()
    distributor_count = Distributer.objects.all().count()
    employee_count = Employee_model.objects.all().count()

    context = {
        'farmer_count': farmer_count,
        'dealer_count': dealer_count,
        'distributor_count': distributor_count,
        'employee_count': employee_count,
    }

    return render(request, 'admin/home.html', context)


@login_required(login_url='/')
def ADD_FARMER(request):

    farmer = EmployeeForm()
    return render(request, 'admin/add_farmer.html', {'farmer': farmer})


@login_required(login_url='/')
def ADD_DISTRIBUTOR(request):

    a = DistributerForm()
    return render(request, 'admin/add_distributor.html', {'a': a})


def ADD_DEALER(request):

    a = DealerForm()
    return render(request, 'admin/add_dealer.html', {'a': a})


def VIEW_EMPLOYEE(request):

    return render(request, 'admin/view_employee.html')


def VIEW_FARMER(request):

    all = Farmer.objects.all()
    return render(request, 'admin/view_farmer.html', {'all': all})


def VIEW_DEALER(request):

    dealer = Dealer.objects.all()
    return render(request, 'admin/view_dealer.html', {'dealer': dealer})


def VIEW_DISTRIBUTOR(request):

    distributer = Distributer.objects.all()
    return render(request, 'admin/view_distributor.html', {'distributer': distributer})


def RESOURCES(request):

    a = Resourse.objects.all()
    print(a)
    return render(request, 'admin/resources.html', {'a': a})


def search(request):

    if 'q' in request.GET:
        q = request.GET['q']
        farmer_q = Q(Q(Name__icontains=q))
        dealer_q = Q(Q(Business_Name__icontains=q))
        distributer_q = Q(Q(Business_Name__icontains=q))

        all = Farmer.objects.filter(farmer_q)
        print("all", len(all))
        dealer = Dealer.objects.filter(dealer_q)
        print("dealer", len(dealer))
        distributer = Distributer.objects.filter(distributer_q)
        print("distributer", len(distributer))

        if (len(all) != 0):
            return render(request, 'admin/view_farmer.html', {'all': all})

        if (len(dealer) != 0):
            return render(request, 'admin/view_dealer.html', {'dealer': dealer})

        elif (len(distributer) != 0):
            return render(request, 'admin/view_distributor.html', {'distributer': distributer})

        else:
            messages.error(request, 'Item not found')
            return render(request, 'search.html')
