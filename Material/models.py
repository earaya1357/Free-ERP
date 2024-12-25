from django.db import models
from django.db.models import Value
from django.db.models.functions import Concat
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser, Group, Permission


class Organization(models.Model):
    organization_name = models.CharField('ORGANIZATION_NAME', max_length=50, null=True, blank=True)
    address = models.CharField('ADDRESS', max_length=75, null=True, blank=True)
    city = models.CharField('CITY', max_length=50, null=True, blank=True)
    state = models.CharField('STATE', max_length=50, null=True, blank=True)
    zip = models.CharField('ZIP', max_length=10, null=True, blank=True)
    country = models.CharField('COUNTRY', max_length=50, null=True, blank=True)
    phone_number = models.CharField('PHONE_NUMBER', max_length=25, null=True, blank=True)
    email = models.EmailField('EMAIL', max_length=50, null=True, blank=True)
    website = models.URLField('WEBSITE', max_length=50, null=True, blank=True)
    notes = models.TextField('NOTES', max_length=250, null=True, blank=True)
    org_id = get_random_string(length=10, allowed_chars='ABCDEFGHJKLMNPQRSTUVWXYZ1234567890')
    org_id = models.CharField('ORG_ID', max_length=10, default=org_id, null=True, blank=True)
    org_password = models.CharField('ORG_PASSWORD', max_length=128, null=True, blank=True)
    org_repassword = models.CharField('ORG_REPASSWORD', max_length=128, null=True, blank=True)
    org_abbreviation = models.CharField('ORG_ABBREVIATION', max_length=6, null=True, blank=True)
    date_created = models.DateField('DATE_CREATED', auto_now_add=True, null=True, blank=True)
    active = models.BooleanField('ACTIVE', default=True, null=True, blank=True)
    organization_logo = models.ImageField('ORGANIZATION_LOGO', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.organization_name



class Company(models.Model):
    associated_organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField('COMPANY_NAME', unique=True, max_length=50, null=True, blank=True)
    company_abbreviation = models.CharField('COMPANY_ABBREVIATION', unique=True, max_length=6, null=True, blank=True)
    address = models.CharField('ADDRESS', max_length=75, null=True, blank=True)
    city = models.CharField('CITY', max_length=50, null=True, blank=True)
    state = models.CharField('STATE', max_length=50, null=True, blank=True)
    zip = models.CharField('ZIP', max_length=10, null=True, blank=True)
    country = models.CharField('COUNTRY', max_length=50, null=True, blank=True)
    phone_number = models.CharField('PHONE_NUMBER', max_length=25, null=True, blank=True)
    email = models.EmailField('EMAIL', max_length=50, null=True, blank=True)
    website = models.URLField('WEBSITE', max_length=50, null=True, blank=True)
    notes = models.TextField('NOTES', max_length=250, null=True, blank=True)
    company_id = get_random_string(length=10, allowed_chars='ABCDEFGHJKLMNPQRSTUVWXYZ1234567890')
    company_id = models.CharField('COMPANY_ID', unique=True, max_length=10, default=company_id, null=True, blank=True)
    company_password = models.CharField('COMPANY_PASSWORD', max_length=128, null=True, blank=True)
    company_repassword = models.CharField('COMPANY_REPASSWORD', max_length=128, null=True, blank=True)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateField('DATE_CREATED', auto_now_add=True, null=True, blank=True)
    active = models.BooleanField('ACTIVE', default=True, null=True, blank=True)
    


    def __str__(self):
        return self.company_abbreviation


class Department(models.Model):
    active = models.BooleanField('ACTIVE', default=True, null=True, blank=True)
    department_name = models.CharField('DEPARTMENT_NAME', unique=True, max_length=50, null=True, blank=True)
    department_abbreviation = models.CharField('DEPARTMENT_ABBREVIATION', unique=True, max_length=12, null=True, blank=True)
    associated_company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    department_id = get_random_string(length=10, allowed_chars='ABCDEFGHJKLMNPQRSTUVWXYZ1234567890')
    department_id = models.CharField('DEPARTMENT_ID', max_length=10, default=department_id, null=True, blank=True)
    date_created = models.DateField('DATE_CREATED', auto_now_add=True, null=True, blank=True)
    notes = models.TextField('NOTES', max_length=250, null=True, blank=True)


    def __str__(self):
        return self.department_abbreviation


class ERPRoles(models.Model):
    active = models.BooleanField('ACTIVE', default=True, null=True, blank=True)
    role = models.CharField('ROLE', unique=True, max_length=50, null=True, blank=True)
    associated_company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True)
    associated_department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True, blank=True)
    description = models.TextField('DESCRIPTION', max_length=150, null=True, blank=True)
    date_created = models.DateField('DATE_CREATED', auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.role


class User(AbstractUser):
    username = models.CharField('USERNAME', unique=True, max_length=30, null=True, blank=True)
    first_name = models.CharField('FIRST_NAME', max_length=30, null=True, blank=True)
    last_name = models.CharField('LAST_NAME', max_length=30, null=True, blank=True)
    password = models.CharField('PASSWORD', max_length=128, null=True, blank=True)
    repassword = models.CharField('REPASSWORD', max_length=128, null=True, blank=True)
    associated_company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True)
    associated_department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True, blank=True)
    role = models.ForeignKey(ERPRoles, on_delete=models.CASCADE,null=True, blank=True)
    phone_number = models.CharField('PHONE_NUMBER', max_length=25, null=True, blank=True)
    address = models.CharField('ADDRESS', max_length=75, null=True, blank=True)
    city = models.CharField('CITY', max_length=50, null=True, blank=True)
    state = models.CharField('STATE', max_length=50, null=True, blank=True)
    zip = models.CharField('ZIP', max_length=10, null=True, blank=True)
    country = models.CharField('COUNTRY', max_length=50, null=True, blank=True)
    notes = models.TextField('NOTES', max_length=250, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='material_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='material_user_permissions_set')
    is_staff = models.BooleanField('STAFF_STATUS', default=False, null=True, blank=True)
    is_active = models.BooleanField('ACTIVE_STATUS', default=True, null=True, blank=True)
    date_joined = models.DateTimeField('DATE_JOINED', auto_now_add=True, null=True, blank=True)
    last_login = models.DateTimeField('LAST_LOGIN', auto_now=True, null=True, blank=True)
    email = models.EmailField('EMAIL', max_length=50, null=True, blank=True)
    user_id = models.CharField('USER_ID', unique=True, max_length=10, default=get_random_string(length=10, allowed_chars='ABCDEFGHJKLMNPQRSTUVWXYZ1234567890'), null=True, blank=True)
    is_superuser = models.BooleanField('SUPERUSER_STATUS', default=False, null=True, blank=True)
    profile_picture = models.ImageField('PROFILE_PICTURE', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Project(models.Model):
    PROJECT_STATUS = (
        ('NOT STARTED','NOT STARTED'),
        ('ON TRACk','ON TRACK'),
        ('OFF TRACK','OFF TRACK'),
        ('COMPLETED','COMPLETED'),
        ('CANCELLED','CANCELLED')
    )
    project_name = models.CharField('PROJECT_NAME', max_length=50, null=True, blank=True)
    project_abbreviation = models.CharField('PROJECT_ABBREVIATION', max_length=6, null=True, blank=True)
    project_id = get_random_string(length=10, allowed_chars='ABCDEFGHJKLMNPQRSTUVWXYZ1234567890')
    project_id = models.CharField('PROJECT_ID', max_length=10, default=project_id, null=True, blank=True)
    project_description = models.TextField('PROJECT_DESCRIPTION', max_length=250, null=True, blank=True)
    project_start_date = models.DateField('PROJECT_START_DATE', null=True, blank=True)
    project_projected_end_date = models.DateField('PROJECT_PROJECTED_END_DATE', null=True, blank=True)
    project_end_date = models.DateField('PROJECT_END_DATE', null=True, blank=True)
    project_manager = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    project_notes = models.TextField('PROJECT_NOTES', max_length=250, null=True, blank=True)
    project_status = models.CharField('PROJECT_STATUS', choices=PROJECT_STATUS, default= 'NOT STARTED',max_length=50, null=True, blank=True)
    date_created = models.DateField('DATE_CREATED', auto_now_add=True, null=True, blank=True)
    active = models.BooleanField('ACTIVE', default=True, null=True, blank=True)

    def __str__(self):
        return self.project_name
    

class ProjectTeam(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True, blank=True)
    team_member = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    team_role = models.CharField('TEAM_ROLE', max_length=50, null=True, blank=True)
    team_start_date = models.DateField('TEAM_START_DATE', null=True, blank=True)
    team_notes = models.TextField('TEAM_NOTES', max_length=250, null=True, blank=True)

    def __str__(self):
        return self.team_member



class SupplierClass(models.Model):
    class_type = models.TextField('CLASS_TYPE', max_length=6, null=True, blank=True)
    description = models.TextField('DESCRIPTION', max_length=150, null=True, blank=True)

    def __str__(self):
        return self.class_type
    


class Supplier(models.Model):
    """Class to support Supplier information"""
    name = models.CharField('NAME', unique=True, max_length=50, null=True, blank=True)
    address = models.CharField('ADDRESS', max_length=75, null=True, blank=True)
    city = models.CharField('CITY', max_length=50, null=True, blank=True)
    country = models.CharField('COUNTRY', max_length=50, null=True, blank=True)
    state = models.CharField('STATE', max_length=50, null=True, blank=True)
    zip = models.CharField('ZIP', max_length=10, null=True, blank=True)
    phone_number = models.CharField('PHONE_NUMBER', max_length=25, null=True, blank=True)
    email = models.EmailField('EMAIL', max_length=50, null=True, blank=True)
    website = models.URLField('WEBSITE', max_length=50, null=True, blank=True)
    approved = models.BooleanField('APPROVED_SUPPLIER', default=False, null=True, blank=True)
    approved_date = models.DateField('APPROVED_DATE', null=True, blank=True)
    approved_by = models.CharField('APPROVED_BY', max_length=50, null=True, blank=True)
    approved_notes = models.TextField('APPROVED_NOTES', max_length=250, null=True, blank=True)
    supplier_class = models.ForeignKey(SupplierClass, on_delete=models.CASCADE,null=True, blank=True)
    notes = models.TextField('NOTES', max_length=250, null=True, blank=True)
    active = models.BooleanField('ACTIVE', default=True, null=True, blank=True)
    last_audit_date = models.DateField('LAST_AUDIT_DATE', null=True, blank=True)
    associated_company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return self.name
    


class PartPrefix(models.Model):
    active = models.BooleanField('ACTIVE', default=True, null=True, blank=True)
    prefix = models.CharField('PREFIX', unique=True, max_length=8, null=True, blank=True)
    prefix_description = models.TextField('DESCRIPTION', max_length=150, null=True, blank=True)

    def __str__(self):
        return self.prefix  



class PartSuffix(models.Model):
    active = models.BooleanField('ACTIVE', default=True, null=True, blank=True)
    suffix = models.CharField('SUFFIX', unique=True, max_length=8, null=True, blank=True)
    suffix_description = models.TextField('DESCRIPTION', max_length=150, null=True, blank=True)

    def __str__(self):
        return self.suffix


class PartNumberType(models.Model):
    active = models.BooleanField('ACTIVE', default=True, null=True, blank=True)
    type = models.CharField('TYPE', unique=True, max_length=50, null=True, blank=True)
    description = models.TextField('DESCRIPTION', max_length=150, null=True, blank=True)

    def __str__(self):
        return self.type


class PartNumberSequence(models.Model):
    type = models.ForeignKey(PartNumberType, on_delete=models.CASCADE, null=True, blank=True)
    prefix = models.ForeignKey(PartPrefix, on_delete=models.CASCADE, null=True, blank=True)
    suffix = models.ForeignKey(PartSuffix, on_delete=models.CASCADE, null=True, blank=True)
    middle = models.CharField('MIDDLE', max_length=10, null=True, blank=True)
    spacer = models.CharField('SPACER', max_length=2, null=True, blank=True)
    description = models.CharField('DESCRIPTION', max_length=150, null=True, blank=True)

    def get_part_number_sequence(self):
        if self.prefix is None:
            self.prefix = ''
        if self.suffix is None:
            self.suffix = ''
        if self.middle is None:
            self.middle = ''
        if self.spacer is None:
            self.spacer = ''
        return str(self.prefix) + str(self.spacer) + str(self.middle) + str(self.spacer) + str(self.suffix)
    
    def __str__(self):
        return self.get_part_number_sequence()
    

class PartClass(models.Model):
    category = models.CharField('CLASS', unique=True, max_length=50, null=True, blank=True)
    description = models.TextField('DESCRIPTION', max_length=150, null=True, blank=True)

    def __str__(self):
        return self.category


class Parts(models.Model):
    LSN = (
        ('LOT','LOT'),
        ('SERIAL','SERIAL'),
        ('N/A','N/A')
        )

    active = models.BooleanField('ACTIVE', default=True, null=True, blank=True)
    associated_project = models.ManyToManyField(Project, default=None, blank=True)
    associated_company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    part_class = models.ForeignKey(PartClass, on_delete=models.CASCADE, null=True, blank=True)
    part_name = models.CharField('PART_NAME', unique=True, max_length=50, null=True, blank=True)
    description = models.CharField('DESCRIPTION', max_length=100, null=True, blank=True)
    lot_serial_number = models.CharField('LOT_SERIAL_NUMBER', max_length=6, choices=LSN,null=True, blank=True)
    part_number_style = models.ForeignKey(PartNumberSequence, on_delete=models.CASCADE, null=True, blank=True)
    revision = models.CharField('REVISION', max_length=6, unique=True, null=True, blank=True)
    base_qty = models.DecimalField('BASE_QTY', decimal_places=4, max_digits=10, null=True, blank=True)
    uom = models.CharField('UNIT_OF_MEASURE', max_length=10, null=True, blank=True)
    part_number = models.CharField('PART_NUMBER', max_length=30, null=True, blank=True)
    price1 = models.DecimalField("PRICE1", decimal_places=4, max_digits=10, null=True, blank=True)
    supplier1 = models.ForeignKey(Supplier, related_name='SUPPLIER1', on_delete=models.CASCADE, null=True, blank=True)
    price2 = models.DecimalField("PRICE2", decimal_places=4, max_digits=10, null=True, blank=True)
    supplier2 = models.ForeignKey(Supplier, related_name='SUPPLIER2', on_delete=models.CASCADE, null=True, blank=True)
    price3 = models.DecimalField("PRICE3", decimal_places=4, max_digits=10, null=True, blank=True)
    supplier3 = models.ForeignKey(Supplier, related_name='SUPPLIER3', on_delete=models.CASCADE, null=True, blank=True)
    inspection = models.BooleanField('INSPECTION_REQUIRED', default=False, null=True, blank=True)
    date_created = models.DateField('DATE_CREATED', auto_now_add=True, null=True, blank=True)
    date_active = models.DateField('DATE_ACTIVE', null=True, blank=True)
    date_inactive = models.DateField('DATE_INACTIVE', null=True, blank=True)
    notes = models.TextField('NOTES', max_length=250, null=True, blank=True)



    def __str__(self):
        return self.part_name




class SerialNumber(models.Model):
    serial_number = models.CharField('SERIAL_NUMBER', max_length=30, null=True, blank=True)
    lot_number = models.CharField('LOT_NUMBER', max_length=6, null=True, blank=True)
    part = models.ForeignKey(Parts, on_delete=models.CASCADE, null=True, blank=True)
    date_generated = models.DateField('DATE_GENERATED', null=True, blank=True)
    notes = models.TextField('NOTES', max_length=250, null=True, blank=True)

    def __str__(self):
        return self.serial_number


class Inventory(models.Model):
    part = models.ForeignKey(Parts, related_name='PART_NUMBER',on_delete=models.CASCADE, null=True, blank=True)
    identifier = models.ForeignKey(SerialNumber, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.DecimalField('QUANTITY', decimal_places=4, max_digits=10, null=True, blank=True)
    description = models.ForeignKey(Parts, related_name='PART_DESCRIPTION',on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField('DATE_ADDED', null=True, blank=True)
    notes = models.TextField('NOTES', max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.part)


class Orders(models.Model):
    order_number = get_random_string(length=10, allowed_chars='ABCDEFG1234567890')
    order_number = models.CharField('ORDER_NUMBER', unique=True, max_length=10, default=order_number, null=True, blank=True)
    associated_project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    requestor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='REQUESTOR',null=True, blank=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='BUYER',null=True, blank=True)
    requested_date = models.DateField('REQUESTED_DATE', null=True, blank=True)
    part1 = models.ForeignKey(Parts,related_name='PART1', on_delete=models.CASCADE, null=True, blank=True)
    part1_qty = models.DecimalField("PART1_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part2 = models.ForeignKey(Parts,related_name='PART2', on_delete=models.CASCADE, null=True, blank=True)
    part2_qty = models.DecimalField("PART2_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part3 = models.ForeignKey(Parts,related_name='PART3', on_delete=models.CASCADE, null=True, blank=True)
    part3_qty = models.DecimalField("PART3_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part4 = models.ForeignKey(Parts,related_name='PART4', on_delete=models.CASCADE, null=True, blank=True)
    part4_qty = models.DecimalField("PART4_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part5 = models.ForeignKey(Parts,related_name='PART5', on_delete=models.CASCADE, null=True, blank=True)
    part5_qty = models.DecimalField("PART5_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part6 = models.ForeignKey(Parts,related_name='PART6', on_delete=models.CASCADE, null=True, blank=True)
    part6_qty = models.DecimalField("PART6_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part7 = models.ForeignKey(Parts,related_name='PART7', on_delete=models.CASCADE, null=True, blank=True)
    part7_qty = models.DecimalField("PART7_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part8 = models.ForeignKey(Parts,related_name='PART8', on_delete=models.CASCADE, null=True, blank=True)
    part8_qty = models.DecimalField("PART8_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part9 = models.ForeignKey(Parts,related_name='PART9', on_delete=models.CASCADE, null=True, blank=True)
    part9_qty = models.DecimalField("PART9_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part10 = models.ForeignKey(Parts,related_name='PART10', on_delete=models.CASCADE, null=True, blank=True)
    part10_qty = models.DecimalField("PART10_QTY", decimal_places=4, max_digits=10, null=True, blank=True)

    def __str__(self):
        return self.order_number



class OrderGroup(models.Model):
    groupordernumber = get_random_string(length=10, allowed_chars='ABCDEFG1234567890')
    groupordernumber = models.CharField('GROUP_ORDER_NUMBER', unique=True,max_length=10, default=groupordernumber, null=True)
    associated_project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    order1 = models.ForeignKey(Orders, related_name='ORDER1', on_delete=models.CASCADE, null=True, blank=True)
    order2 = models.ForeignKey(Orders, related_name='ORDER2', on_delete=models.CASCADE, null=True, blank=True)
    order3 = models.ForeignKey(Orders, related_name='ORDER3', on_delete=models.CASCADE, null=True, blank=True)
    order4 = models.ForeignKey(Orders, related_name='ORDER4', on_delete=models.CASCADE, null=True, blank=True)
    order5 = models.ForeignKey(Orders, related_name='ORDER5', on_delete=models.CASCADE, null=True, blank=True)
    order6 = models.ForeignKey(Orders, related_name='ORDER6', on_delete=models.CASCADE, null=True, blank=True)
    order7 = models.ForeignKey(Orders, related_name='ORDER7', on_delete=models.CASCADE, null=True, blank=True)
    order8 = models.ForeignKey(Orders, related_name='ORDER8', on_delete=models.CASCADE, null=True, blank=True)
    order9 = models.ForeignKey(Orders, related_name='ORDER9', on_delete=models.CASCADE, null=True, blank=True)
    order10 = models.ForeignKey(Orders, related_name='ORDER10', on_delete=models.CASCADE, null=True, blank=True)
    order11 = models.ForeignKey(Orders, related_name='ORDER11', on_delete=models.CASCADE, null=True, blank=True)
    order12 = models.ForeignKey(Orders, related_name='ORDER12', on_delete=models.CASCADE, null=True, blank=True)
    order13 = models.ForeignKey(Orders, related_name='ORDER13', on_delete=models.CASCADE, null=True, blank=True)
    order14 = models.ForeignKey(Orders, related_name='ORDER14', on_delete=models.CASCADE, null=True, blank=True)
    order15 = models.ForeignKey(Orders, related_name='ORDER15', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.groupordernumber

