# Generated by Django 4.0 on 2022-09-10 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_delete_userblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userblock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('blocked_date', models.DateField(auto_now_add=True)),
                ('blocked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block', to='users.account')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
            ],
        ),
    ]