# Generated by Django 4.0 on 2022-09-11 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_userblock'),
        ('blockUser', '0003_alter_userblock_blocked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userblock',
            name='owner',
        ),
        migrations.AddField(
            model_name='userblock',
            name='block_owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='block_owner', to='users.account'),
        ),
    ]
