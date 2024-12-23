# Generated by Django 5.1.4 on 2024-12-24 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Material", "0035_erproles_associated_company_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="erproles",
            name="date_created",
            field=models.DateField(
                auto_now_add=True, null=True, verbose_name="DATE_CREATED"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="company_id",
            field=models.CharField(
                blank=True,
                default="Y7JAVLPU8C",
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
                default="856V80VYMX",
                max_length=10,
                null=True,
                verbose_name="DEPARTMENT_ID",
            ),
        ),
        migrations.AlterField(
            model_name="ordergroup",
            name="groupordernumber",
            field=models.CharField(
                default="8C2115C852",
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
                default="D3850225CB",
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
                default="5AKSYLXJCR",
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
                default="W28NMPK6MA",
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
                default="6XVBXXDGW7",
                max_length=10,
                null=True,
                unique=True,
                verbose_name="USER_ID",
            ),
        ),
    ]
