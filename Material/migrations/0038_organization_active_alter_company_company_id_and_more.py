# Generated by Django 5.1.4 on 2024-12-24 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Material", "0037_department_active_erproles_active_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
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
                default="UHWGUTCCQ8",
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
                default="BPKA8HGT91",
                max_length=10,
                null=True,
                verbose_name="DEPARTMENT_ID",
            ),
        ),
        migrations.AlterField(
            model_name="ordergroup",
            name="groupordernumber",
            field=models.CharField(
                default="1A90GCF128",
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
                default="40F9A7EG37",
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
                default="GLLN0F48NT",
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
                default="1KJK494LQD",
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
                default="ARQT6EWB04",
                max_length=10,
                null=True,
                unique=True,
                verbose_name="USER_ID",
            ),
        ),
    ]
