from django.forms import ModelForm
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['is_superuser', 'is_staff','groups', 'user_permissions']


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


class ProjectTeamForm(ModelForm):
    class Meta:
        model = ProjectTeam
        fields = '__all__'


class PartNumberTypeForm(ModelForm):
    class Meta:
        model = PartNumberType
        fields = '__all__'

class PartClassForm(ModelForm):
    class Meta:
        model = PartClass
        fields = '__all__'


class PartPrefixForm(ModelForm):
    class Meta:
        model = PartPrefix
        fields = '__all__'


class PartSuffixForm(ModelForm):
    class Meta:
        model = PartSuffix
        fields = '__all__'


class PartNumberSequenceForm(ModelForm):
    class Meta:
        model = PartNumberSequence
        fields = '__all__'


class PartsForm(ModelForm):
    class Meta:
        model = Parts
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

