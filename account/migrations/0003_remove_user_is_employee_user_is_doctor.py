# Generated by Django 4.2 on 2023-06-21 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_mymodel_remove_user_is_customer_user_is_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_employee',
        ),
        migrations.AddField(
            model_name='user',
            name='is_doctor',
            field=models.BooleanField(default=False, verbose_name='Is doctor'),
        ),
    ]
