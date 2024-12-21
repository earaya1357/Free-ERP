from django.shortcuts import render, redirect
from .forms import *
from .models import *


def home(request):
    return render(request, 'index.html')

##### Organization Section #####
def organizations(request):
    try:
        organizations = Organization.objects.get(id=1)
        companies = Company.objects.filter(associated_organization=organizations)
    except Organization.DoesNotExist:
        organizations = None
        companies = None
    
    form1 = OrganizationForm()
    form2 = CompanyForm()
    
    if request.method == 'POST':
        
        if request.POST.get('form-submit') == 'org-form':
            form = OrganizationForm(request.POST)
            if form.is_valid():
                form.save()
                print(form.data)
                return redirect('organizations')
            else:
                form1 = OrganizationForm(request.POST, instance=form.instance)
                return redirect('organizations')
        elif request.POST.get('form-submit') == 'company-form':
            form = CompanyForm(request.POST)
            if form.is_valid():
                form.save()
                print(form.data)
                return redirect('organizations')
            else:
                form2 = CompanyForm(request.POST, instance=form.instance)
                return redirect('organizations')
        else:
            return redirect('organizations')
        
    
    return render(request, 'organizations.html', context={'organizations': organizations, 'companies': companies, 'org_form':form1, 'company_form':form2})


##### Order Section #####

# def orders(request):
#     return render(request, 'orders.html')



##### Material Section #####
def inventory(request):
    return render(request, 'inventory.html')



##### Supplier Section #####
def suppliers(request):
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            #form.save()
            print(form.data)
    else:
        form = SupplierForm()
    return render(request, 'suppliers.html', context={'form': form, 'suppliers': suppliers})
