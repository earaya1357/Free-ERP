from django.db import models
from django.db.models import Value
from django.db.models.functions import Concat
from django.utils.crypto import get_random_string




class Supplier(models.Model):
    """Class to support Supplier information"""
    name = models.CharField('NAME', max_length=50, null=True, blank=True)
    address = models.CharField('ADDRESS', max_length=75, null=True, blank=True)
    country = models.CharField('COUNTRY', max_length=50, null=True, blank=True)
    approved = models.BooleanField('APPROVED_SUPPLIER', default=False, null=True, blank=True)
    supplier_class = models.CharField('SUPPLIER_CLASS', max_length=10, null=True, blank=True)
    notes = models.TextField('NOTES', max_length=250, null=True, blank=True)



class PartPrefix(models.Model):
    prefix = models.CharField('PREFIX', max_length=8, null=True, blank=True)



class PartSuffix(models.Model):
    suffix = models.CharField('SUFFIX', max_length=8, null=True, blank=True)



class PartNumberSequence(models.Model):
    prefix = models.ForeignKey(PartPrefix, on_delete=models.CASCADE, null=True, blank=True)
    suffix = models.ForeignKey(PartSuffix, on_delete=models.CASCADE, null=True, blank=True)
    middle = models.CharField('MIDDLE', max_length=10, null=True, blank=True)
    spacer = models.CharField('SPACER', max_length=2, null=True, blank=True)

    def get_part_number_sequence(self):
        return Concat('prefix', Value('spacer'), 'middle',Value('spacer'), 'suffix')



class Parts(models.Model):
    part_name = models.CharField('PART_NAME', max_length=50, null=True, blank=True)
    description = models.CharField('DESCRIPTION', max_length=100, null=True, blank=True)
    part_number_style = models.ForeignKey(PartNumberSequence, on_delete=models.CASCADE, null=True, blank=True)
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


class Orders(models.Model):
    part1 = models.ForeignKey(Parts,related_name='PART1', on_delete=models.CASCADE, null=True, blank=True)
    part1_qty = models.DecimalField("PART1_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part1_due_date = models.DateField("PART1_DUE_DATE", null=True, blank=True)
    part2 = models.ForeignKey(Parts,related_name='PART2', on_delete=models.CASCADE, null=True, blank=True)
    part2_qty = models.DecimalField("PART2_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part2_due_date = models.DateField("PART2_DUE_DATE", null=True, blank=True)
    part3 = models.ForeignKey(Parts,related_name='PART3', on_delete=models.CASCADE, null=True, blank=True)
    part3_qty = models.DecimalField("PART3_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part3_due_date = models.DateField("PART3_DUE_DATE", null=True, blank=True)
    part4 = models.ForeignKey(Parts,related_name='PART4', on_delete=models.CASCADE, null=True, blank=True)
    part4_qty = models.DecimalField("PART4_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part4_due_date = models.DateField("PART4_DUE_DATE", null=True, blank=True)
    part5 = models.ForeignKey(Parts,related_name='PART5', on_delete=models.CASCADE, null=True, blank=True)
    part5_qty = models.DecimalField("PART5_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part5_due_date = models.DateField("PART5_DUE_DATE", null=True, blank=True)
    part6 = models.ForeignKey(Parts,related_name='PART6', on_delete=models.CASCADE, null=True, blank=True)
    part6_qty = models.DecimalField("PART6_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part6_due_date = models.DateField("PART6_DUE_DATE", null=True, blank=True)
    part7 = models.ForeignKey(Parts,related_name='PART7', on_delete=models.CASCADE, null=True, blank=True)
    part7_qty = models.DecimalField("PART7_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part7_due_date = models.DateField("PART7_DUE_DATE", null=True, blank=True)
    part8 = models.ForeignKey(Parts,related_name='PART8', on_delete=models.CASCADE, null=True, blank=True)
    part8_qty = models.DecimalField("PART8_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part8_due_date = models.DateField("PART8_DUE_DATE", null=True, blank=True)
    part9 = models.ForeignKey(Parts,related_name='PART9', on_delete=models.CASCADE, null=True, blank=True)
    part9_qty = models.DecimalField("PART9_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part9_due_date = models.DateField("PART9_DUE_DATE", null=True, blank=True)
    part10 = models.ForeignKey(Parts,related_name='PART10', on_delete=models.CASCADE, null=True, blank=True)
    part10_qty = models.DecimalField("PART10_QTY", decimal_places=4, max_digits=10, null=True, blank=True)
    part10_due_date = models.DateField("PART10_DUE_DATE", null=True, blank=True)



class OrderGroup(models.Model):
    #groupordernumber = get_random_string(length=10, allowed_chars='ABCDEFG1234567890')
    #groupordernumber = models.CharField('GROUP_ORDER_NUMBER',max_length=10, default=groupordernumber, null=True)
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


