# Generated by Django 5.1.2 on 2024-12-03 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0006_rename_employe_promotionne_handicap_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_fin', models.DateField()),
                ('type_contrat', models.CharField(choices=[('CDI', 'Contrat à Durée Indéterminée'), ('CDD', 'Contrat à Durée Déterminée'), ('Stage', 'Stage'), ('Freelance', 'Freelance')], max_length=50)),
                ('raison_fin', models.TextField()),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finactivities', to='EmployeeApp.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finactivities', to='EmployeeApp.employee')),
            ],
        ),
    ]