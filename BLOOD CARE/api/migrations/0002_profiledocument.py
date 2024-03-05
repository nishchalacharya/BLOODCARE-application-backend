# Generated by Django 4.2.6 on 2024-03-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('profilepic', models.ImageField(upload_to='document_pictures')),
            ],
        ),
    ]
