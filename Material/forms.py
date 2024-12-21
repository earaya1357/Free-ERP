from django.forms import ModelForm
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ERPRoleForm(ModelForm):
    class Meta:
        model = ERPRoles
        fields = '__all__'


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class PartPrefixForm(ModelForm):
    class Meta:
        model = PartPrefix
        fields = '__all__'


class PartSuffixForm(ModelForm):
    class Meta:
        model = PartSuffix
        fields = '__all__'


class PartNumberSequence(ModelForm):
    class Meta:
        model = PartNumberSequence
        fields = '__all__'


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'



class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'address', 'city', 'country', 'state', 'zip', 'phone_number', 'email', 'website', 'supplier_class','notes']


class SupplierClassForm(ModelForm):
    class Meta:
        model = SupplierClass
        fields = ['class_type', 'description']

