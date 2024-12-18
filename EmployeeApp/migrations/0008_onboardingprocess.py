# Generated by Django 5.1.2 on 2024-12-03 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0007_finactivity'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnboardingProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('contract_type', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('poste', models.CharField(blank=True, max_length=255, null=True)),
                ('societe', models.CharField(blank=True, max_length=255, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('account_activated', models.CharField(max_length=50)),
                ('remote_work', models.BooleanField(default=False)),
                ('on_site_work', models.BooleanField(default=False)),
                ('work_hours', models.CharField(max_length=255)),
                ('document_submission', models.CharField(max_length=255)),
                ('id_card_application', models.BooleanField(default=False)),
                ('motorized_parking', models.BooleanField(default=False)),
                ('emergency_contact', models.CharField(max_length=255)),
                ('onboarding_rating', models.IntegerField()),
                ('positive_feedback', models.TextField(blank=True, null=True)),
                ('improvements_feedback', models.TextField(blank=True, null=True)),
                ('advice_feedback', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
