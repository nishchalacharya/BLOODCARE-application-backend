# Generated by Django 5.0.2 on 2024-03-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donordetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prov_no', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('bloodgrp', models.CharField(max_length=5)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('phoneno', models.CharField(max_length=10)),
                ('confirm', models.BooleanField(default=False)),
                ('lattitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
                ('emailid', models.EmailField(max_length=254)),
                ('phoneno', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='profimages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(upload_to='profile_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='requestdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_name', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=50)),
                ('bloodgroup', models.CharField(max_length=10)),
                ('prov_no', models.CharField(max_length=2)),
                ('district', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=75)),
                ('reqpint', models.IntegerField(default=1)),
                ('phoneno', models.CharField(max_length=10)),
                ('req_date', models.DateField()),
                ('case_details', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward_point', models.IntegerField(default=0.0)),
            ],
        ),
    ]