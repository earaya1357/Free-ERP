from django.db import models
from django.db.models import Value
from django.db.models.functions import Concat



class Supplier(models.Model):
    """Class to support Supplier information"""
    name = models.CharField('NAME', max_length=50)
    address = models.CharField('ADDRESS', max_length=75)
    country = models.CharField('COUNTRY', max_length=50)
    approved = models.BooleanField('APPROVED_SUPPLIER', default=False)
    supplier_class = models.CharField('SUPPLIER_CLASS', max_length=10)
    notes = models.TextField('NOTES', max_length=250)



class PartPrefix(models.Model):
    prefix = models.CharField('PREFIX', max_length=8)



class PartSuffix(models.Model):
    suffix = models.CharField('SUFFIX', max_length=8)



class PartNumberSequence(models.Model):
    prefix = models.OneToOneField(PartPrefix, on_delete=models.CASCADE)
    suffix = models.OneToOneField(PartSuffix, on_delete=models.CASCADE)
    middle = models.CharField('MIDDLE', max_length=10)
    spacer = models.CharField('SPACER', max_length=2)

    def get_part_number_sequence(self):
        return Concat('prefix', Value('spacer'), 'middle',Value('spacer'), 'suffix')



class Parts(models.Model):
    partname = models.CharField('PART_NAME', max_length=50)
    description = models.CharField('DESCRIPTION', max_length=100)
    partnumberstyle = models.OneToOneField(PartNumberSequence, on_delete=models.CASCADE)
    partnumber = models.CharField('PART_NUMBER', max_length=30)
    price = models.FloatField("PRICE", max_length=8)
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE)
    inspection = models.BooleanField('INSPECTION_REQUIRED', default=False)


class OrderGroup(models.Model):
    pass

class Orders(models.Model):
    pass


    
