# Generated by Django 5.1.4 on 2024-12-21 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Material", "0027_organization_organization_logo_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="parts",
            name="associated_company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Material.company",
            ),
        ),
        migrations.AddField(
            model_name="parts",
            name="associated_project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Material.project",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="project_status",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="PROJECT_STATUS"
            ),
        ),
        migrations.AddField(
            model_name="supplier",
            name="associated_company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Material.company",
            ),
        ),
        migrations.AddField(
            model_name="supplier",
            name="last_audit_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="LAST_AUDIT_DATE"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="company_abbreviation",
            field=models.CharField(
                blank=True,
                max_length=6,
                null=True,
                unique=True,
                verbose_name="COMPANY_ABBREVIATION",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="company_id",
            field=models.CharField(
                blank=True,
                default="VTLFUJ46C1",
                max_length=10,
                null=True,
                unique=True,
                verbose_name="COMPANY_ID",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="company_name",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                unique=True,
                verbose_name="COMPANY_NAME",
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="department_abbreviation",
            field=models.CharField(
                blank=True,
                max_length=12,
                null=True,
                unique=True,
                verbose_name="DEPARTMENT_ABBREVIATION",
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="department_id",
            field=models.CharField(
                blank=True,
                default="6QM8KB5G64",
                max_length=10,
                null=True,
                verbose_name="DEPARTMENT_ID",
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="department_name",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                unique=True,
                verbose_name="DEPARTMENT_NAME",
            ),
        ),
        migrations.AlterField(
            model_name="erproles",
            name="role",
            field=models.CharField(
                blank=True, max_length=50, null=True, unique=True, verbose_name="ROLE"
            ),
        ),
        migrations.AlterField(
            model_name="ordergroup",
            name="groupordernumber",
            field=models.CharField(
                default="5E1848E37C",
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
                default="85BC960055",
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
                default="9541TRBMES",
                max_length=10,
                null=True,
                verbose_name="ORG_ID",
            ),
        ),
        migrations.AlterField(
            model_name="partprefix",
            name="prefix",
            field=models.CharField(
                blank=True, max_length=8, null=True, unique=True, verbose_name="PREFIX"
            ),
        ),
        migrations.AlterField(
            model_name="parts",
            name="part_name",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                unique=True,
                verbose_name="PART_NAME",
            ),
        ),
        migrations.AlterField(
            model_name="partsuffix",
            name="suffix",
            field=models.CharField(
                blank=True, max_length=8, null=True, unique=True, verbose_name="SUFFIX"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="project_id",
            field=models.CharField(
                blank=True,
                default="4NK79N3SYS",
                max_length=10,
                null=True,
                verbose_name="PROJECT_ID",
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="name",
            field=models.CharField(
                blank=True, max_length=50, null=True, unique=True, verbose_name="NAME"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                blank=True,
                default="ZYUTPT9BMC",
                max_length=10,
                null=True,
                unique=True,
                verbose_name="USER_ID",
            ),
        ),
    ]
