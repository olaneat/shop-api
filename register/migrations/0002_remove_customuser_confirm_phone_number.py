# Generated by Django 2.1.4 on 2020-02-13 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='confirm_phone_number',
        ),
    ]