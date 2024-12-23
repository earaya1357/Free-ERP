# Generated by Django 5.1.4 on 2024-12-24 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Material", "0036_erproles_date_created_alter_company_company_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="active",
            field=models.BooleanField(
                blank=True, default=True, null=True, verbose_name="ACTIVE"
            ),
        ),
        migrations.AddField(
            model_name="erproles",
            name="active",
            field=models.BooleanField(
                blank=True, default=True, null=True, verbose_name="ACTIVE"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="company_id",
            field=models.CharField(
                blank=True,
                default="T7CZEYKNPK",
                max_length=10,
                null=True,
                unique=True,
                verbose_name="COMPANY_ID",
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="department_id",
            field=models.CharField(
                blank=True,
                default="FPR79C21CR",
                max_length=10,
                null=True,
                verbose_name="DEPARTMENT_ID",
            ),
        ),
        migrations.AlterField(
            model_name="ordergroup",
            name="groupordernumber",
            field=models.CharField(
                default="DCD62FG56F",
                max_length=10,
                null=True,
                unique=True,
                verbose_name="GROUP_ORDER_NUMBER",
            ),
        ),
        migrations.AlterField(
            model_name="orders",
            name="order_number",
            field=models.CharField(
                blank=True,
                default="C8747DD2D5",
                max_length=10,
                null=True,
                unique=True,
                verbose_name="ORDER_NUMBER",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="org_id",
            field=models.CharField(
                blank=True,
                default="3DF5JUD0H3",
                max_length=10,
                null=True,
                verbose_name="ORG_ID",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="project_id",
            field=models.CharField(
                blank=True,
                default="L43TWXW9S5",
                max_length=10,
                null=True,
                verbose_name="PROJECT_ID",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                blank=True,
                default="QWL93YLXS3",
                max_length=10,
                null=True,
                unique=True,
                verbose_name="USER_ID",
            ),
        ),
    ]
