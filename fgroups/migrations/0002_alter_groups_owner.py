# Generated by Django 4.0 on 2022-09-14 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_userblock'),
        ('fgroups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_owner', to='users.account'),
        ),
    ]