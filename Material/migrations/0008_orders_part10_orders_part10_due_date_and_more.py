# Generated by Django 5.1.4 on 2024-12-19 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Material",
            "0007_remove_orders_part10_remove_orders_part10_due_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="part10",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PART10",
                to="Material.parts",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part10_due_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="PART10_DUE_DATE"
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part10_qty",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="PART10_QTY",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part1_due_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="PART1_DUE_DATE"
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part1_qty",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="PART1_QTY",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PART2",
                to="Material.parts",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part2_due_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="PART2_DUE_DATE"
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part2_qty",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="PART2_QTY",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part3",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PART3",
                to="Material.parts",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part3_due_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="PART3_DUE_DATE"
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part3_qty",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="PART3_QTY",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part4",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PART4",
                to="Material.parts",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part4_due_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="PART4_DUE_DATE"
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part4_qty",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="PART4_QTY",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part5",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PART5",
                to="Material.parts",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part5_due_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="PART5_DUE_DATE"
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part5_qty",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="PART5_QTY",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part6",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PART6",
                to="Material.parts",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part6_due_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="PART6_DUE_DATE"
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part6_qty",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="PART6_QTY",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part7",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PART7",
                to="Material.parts",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part7_due_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="PART7_DUE_DATE"
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part7_qty",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="PART7_QTY",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part8",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PART8",
                to="Material.parts",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part8_due_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="PART8_DUE_DATE"
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part8_qty",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="PART8_QTY",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part9",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PART9",
                to="Material.parts",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part9_due_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="PART9_DUE_DATE"
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="part9_qty",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="PART9_QTY",
            ),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="description",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PART_DESCRIPTION",
                to="Material.parts",
            ),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="part",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PART_NUMBER",
                to="Material.parts",
            ),
        ),
        migrations.AlterField(
            model_name="ordergroup",
            name="groupordernumber",
            field=models.CharField(
                default="331523862D",
                max_length=10,
                null=True,
                verbose_name="GROUP_ORDER_NUMBER",
            ),
        ),
        migrations.AlterField(
            model_name="orders",
            name="order_number",
            field=models.CharField(
                blank=True,
                default="659181433D",
                max_length=10,
                null=True,
                verbose_name="ORDER_NUMBER",
            ),
        ),
        migrations.AlterField(
            model_name="orders",
            name="part1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="PART1",
                to="Material.parts",
            ),
        ),
        migrations.AlterField(
            model_name="serialnumber",
            name="serial_number",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="SERIAL_NUMBER"
            ),
        ),
    ]