# Generated by Django 4.2.6 on 2024-03-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('documentpic', models.ImageField(upload_to='document_pictures')),
                ('isverified', models.BooleanField(default=False)),
            ],
        ),
    ]