# Generated by Django 5.0.3 on 2024-03-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password_reset_otp_secret',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
