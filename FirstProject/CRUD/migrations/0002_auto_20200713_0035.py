# Generated by Django 3.0.8 on 2020-07-12 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='eAdddress',
            new_name='eAddress',
        ),
    ]