# Generated by Django 4.0 on 2021-12-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_doctor_employee_office_position_specialization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='office_number',
            field=models.CharField(max_length=4),
        ),
    ]