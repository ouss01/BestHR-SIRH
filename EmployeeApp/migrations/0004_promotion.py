# Generated by Django 5.1.2 on 2024-11-29 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0003_alter_employee_employeeid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_promotion', models.DateField()),
                ('designation_avant', models.CharField(max_length=255)),
                ('designation_apres', models.CharField(max_length=255)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to='EmployeeApp.department')),
                ('employe_promotionne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to='EmployeeApp.employee')),
            ],
        ),
    ]
