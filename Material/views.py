from django.shortcuts import render, redirect
from .forms import *
from .models import *


def admin(request):
    try:
        organizations = Organization.objects.get(id=1)
        companies = Company.objects.filter(associated_organization=organizations)
    except Organization.DoesNotExist:
        print('Organization does not exist')
        organizations = None
        companies = None
    return render(request, 'admin.html', context={'organizations': organizations, 'companies': companies})



def users(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.data)
            redirect('users')
    else:
        form = UserForm()
    return render(request, 'users.html', context={'user_form': form, 'users': users})



def home(request):
    try:
        organizations = Organization.objects.get(id=1)
        companies = Company.objects.filter(associated_organization=organizations)
    except Organization.DoesNotExist:
        print('Organization does not exist')
        organizations = None
        companies = None
    return render(request, 'index.html', context={'organizations': organizations, 'companies': companies})

##### Organization Section #####
def organizations(request):
    try:
        organizations = Organization.objects.get(id=1)
        companies = Company.objects.filter(associated_organization=organizations)
        departments = Department.objects.all()
        roles = ERPRoles.objects.all()
    except Organization.DoesNotExist:
        organizations = None
        companies = None
        departments = None
        roles = None
    
    form1 = OrganizationForm()
    form2 = CompanyForm()
    form3 = DepartmentForm()
    form4 = ERPRoleForm()
    
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
        elif request.POST.get('form-submit') == 'department-form':
            form = DepartmentForm(request.POST)
            if form.is_valid():
                form.save()
                print(form.data)
                return redirect('organizations')
            else:
                form3 = DepartmentForm(request.POST, instance=form.instance)
                return redirect('organizations')
        elif request.POST.get('form-submit') == 'role-form':
            form = ERPRoleForm(request.POST)
            if form.is_valid():
                form.save()
                print(form.data)
                return redirect('organizations')
            else:
                form4 = ERPRoleForm(request.POST, instance=form.instance)
                return redirect('organizations')
        else:
            return redirect('organizations')
    
    context = {
        'organizations': organizations,
        'companies': companies,
        'departments': departments,
        'roles': roles,
        'org_form': form1,
        'company_form': form2,
        'department_form': form3,
        'role_form': form4
    }
    
    return render(request, 'organizations.html', context=context)


##### Order Section #####

# def orders(request):
#     return render(request, 'orders.html')



##### Material Section #####
def inventory(request):
    inventory = Inventory.objects.all()
    context={'inventory': inventory}
    return render(request, 'inventory.html', context=context)


def parts(request):
    parts = Parts.objects.all()
    prefix = PartPrefix.objects.all()
    suffix = PartSuffix.objects.all()
    sequence = PartNumberSequence.objects.all()
    part_class = PartClass.objects.all
    part_sequence_type = PartNumberType.objects.all()

    part_form = PartsForm()
    prefix_form = PartPrefixForm()
    suffix_form = PartSuffixForm()
    sequence_form = PartNumberSequenceForm()
    part_class_form = PartClassForm()
    part_sequence_type_form = PartNumberTypeForm()

    if request.POST.get('form-submit') == 'part-form':
        form = PartsForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.data)
            redirect('parts')
    elif request.POST.get('form-submit') == 'prefix-form':
        prefix_form = PartPrefixForm(request.POST)
        if prefix_form.is_valid():
            prefix_form.save()
            print(prefix_form.data)
            redirect('parts')
    elif request.POST.get('form-submit') == 'suffix-form':
        suffix_form = PartSuffixForm(request.POST)
        if suffix_form.is_valid():
            suffix_form.save()
            print(suffix_form.data)
            redirect('parts')
    elif request.POST.get('form-submit') == 'sequence-form':
        sequence_form = PartNumberSequenceForm(request.POST)
        if sequence_form.is_valid():
            sequence_form.save()
            print(sequence_form.data)
            redirect('parts')
    elif request.POST.get('form-submit') == 'part-class-form':
        part_class = PartClassForm(request.POST)
        if part_class.is_valid():
            part_class.save()
            print(part_class.data)
            redirect('parts')
    elif request.POST.get('form-submit') == 'sequence-type-form':
        part_sequence_type_form = PartNumberTypeForm(request.POST)
        if part_sequence_type_form.is_valid():
            part_sequence_type_form.save()
            print(part_sequence_type_form.data)
            redirect('parts')
    else:
        part_form = PartsForm()
        prefix_form = PartPrefixForm()
        suffix_form = PartSuffixForm()
        sequence_form = PartNumberSequenceForm()
        part_class_form = PartClassForm()
        part_sequence_type_form = PartNumberTypeForm()


    context={'part_form': part_form, 
             'prefix_form': prefix_form, 
             'suffix_form': suffix_form, 
             'sequence_form': sequence_form,
             'part_sequence_type_form': part_sequence_type_form,
             'part_class_form': part_class_form,
             'parts': parts, 
             'prefix': prefix, 
             'suffix': suffix, 
             'sequence': sequence,
             'part_class': part_class,
             'part_sequence_type': part_sequence_type
             }

    return render(request, 'parts.html', context=context)



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



##### Project Section #####
def projects(request):
    projects = Project.objects.all()
    project_teams = ProjectTeam.objects.all()
    project_form = ProjectForm()
    project_team_form = ProjectTeamForm()

    if request.POST.get('form-submit') == 'project-form':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.save()
            print(project_form.data)
            redirect('projects')
    elif request.POST.get('form-submit') == 'project-team-form':
        project_team_form = ProjectTeamForm(request.POST)
        if project_team_form.is_valid():
            project_team_form.save()
            print(project_team_form.data)
            redirect('projects')
    else:
        project_form = ProjectForm()
        project_team_form = ProjectTeamForm()

    context = {'project_form': project_form, 
               'project_team_form': project_team_form,
               'projects': projects,
               'project_teams': project_teams
               }
    return render(request, 'projects.html', context=context)
