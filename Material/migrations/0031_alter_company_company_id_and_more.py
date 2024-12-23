# Generated by Django 5.1.4 on 2024-12-23 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Material", "0030_alter_company_company_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="company_id",
            field=models.CharField(
                blank=True,
                default="9AAK3BFV17",
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
                default="DGH5RU6KBK",
                max_length=10,
                null=True,
                verbose_name="DEPARTMENT_ID",
            ),
        ),
        migrations.AlterField(
            model_name="ordergroup",
            name="groupordernumber",
            field=models.CharField(
                default="BE9CA5G260",
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
                default="773899995B",
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
                default="M21BTSRK9A",
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
                default="H4AGCTA5XK",
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
                default="U7LE8TV68N",
                max_length=10,
                null=True,
                unique=True,
                verbose_name="USER_ID",
            ),
        ),
    ]
