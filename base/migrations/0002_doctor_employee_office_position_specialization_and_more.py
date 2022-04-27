# Generated by Django 4.0 on 2021-12-13 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('gender', models.CharField(blank=True, choices=[('м', 'Мужской'), ('ж', 'Женский'), ('н', 'Не указано')], default='н', max_length=1)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('record_book_id', models.CharField(blank=True, max_length=7, null=True)),
                ('passport_id', models.CharField(blank=True, max_length=11, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['full_name']},
        ),
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='full_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('м', 'Мужской'), ('ж', 'Женский'), ('н', 'Не указано')], default='н', max_length=1),
        ),
        migrations.AddField(
            model_name='patient',
            name='passport_id',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('office', models.ManyToManyField(to='base.Office')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(choices=[('пн', 'Понедельник'), ('вт', 'Вторник'), ('ср', 'Среда'), ('чт', 'Четверг'), ('пт', 'Пятница'), ('сб', 'Суббота'), ('вс', 'Воскресенье')], max_length=2)),
                ('work_start_time', models.TimeField()),
                ('work_end_time', models.TimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
            ],
            options={
                'ordering': ['employee', 'weekday'],
            },
        ),
        migrations.CreateModel(
            name='MedicalTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('name', models.CharField(max_length=255)),
                ('result', models.CharField(max_length=1000)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.doctor')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.office')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.patient')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.service')),
            ],
            options={
                'ordering': ['name', 'date'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.position'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.employee'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.specialization'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('patient_complaints', models.CharField(blank=True, max_length=1000, null=True)),
                ('anamnesis', models.CharField(blank=True, max_length=1000, null=True)),
                ('examination_result', models.CharField(blank=True, max_length=1000, null=True)),
                ('diagnosis', models.CharField(blank=True, max_length=1000, null=True)),
                ('recommendations', models.CharField(blank=True, max_length=1000, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.doctor')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.office')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.patient')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.service')),
            ],
            options={
                'ordering': ['date', 'doctor'],
            },
        ),
    ]
