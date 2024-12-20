# myapp/admin.py
from django.contrib import admin
from .models import *

admin.site.register(PartNumberSequence)
admin.site.register(PartPrefix)
admin.site.register(PartSuffix)
admin.site.register(Parts)
admin.site.register(Supplier)
admin.site.register(Orders)
admin.site.register(OrderGroup)
admin.site.register(Inventory)
admin.site.register(SerialNumber)
admin.site.register(SupplierClass)
admin.site.register(Organization)
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(ProjectTeam)

