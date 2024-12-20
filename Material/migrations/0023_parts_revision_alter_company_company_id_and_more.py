# Generated by Django 5.1.4 on 2024-12-21 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Material", "0022_company_department_organization_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="parts",
            name="revision",
            field=models.CharField(
                blank=True, max_length=6, null=True, verbose_name="REVISION"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="company_id",
            field=models.CharField(
                blank=True,
                default="V7JYNKR20A",
                max_length=10,
                null=True,
                verbose_name="COMPANY_ID",
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="department_id",
            field=models.CharField(
                blank=True,
                default="ZVYY2CGY2L",
                max_length=10,
                null=True,
                verbose_name="DEPARTMENT_ID",
            ),
        ),
        migrations.AlterField(
            model_name="ordergroup",
            name="groupordernumber",
            field=models.CharField(
                default="225FGFCD82",
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
                default="ED7A391BC2",
                max_length=10,
                null=True,
                verbose_name="ORDER_NUMBER",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="org_id",
            field=models.CharField(
                blank=True,
                default="A0N5FZX6R9",
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
                default="AHL90R72RD",
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
                default="SYRABEQYM9",
                max_length=10,
                null=True,
                verbose_name="USER_ID",
            ),
        ),
    ]
