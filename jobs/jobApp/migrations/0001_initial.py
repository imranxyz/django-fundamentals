# Generated by Django 2.2.2 on 2022-09-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blorejobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Blorejobs',
            },
        ),
        migrations.CreateModel(
            name='Hydjobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Hydjobs',
            },
        ),
        migrations.CreateModel(
            name='Kolkatajobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Kolkatajobs',
            },
        ),
        migrations.CreateModel(
            name='Punejobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Punejobs',
            },
        ),
    ]
