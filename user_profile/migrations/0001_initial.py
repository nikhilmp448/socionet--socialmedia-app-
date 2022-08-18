# Generated by Django 4.0 on 2022-08-10 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default='male', max_length=20)),
                ('dob', models.DateField(blank=True, default=None, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('works_at', models.CharField(blank=True, max_length=200, null=True)),
                ('lives_in', models.CharField(blank=True, max_length=200, null=True)),
                ('studies_at', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_data', to='users.account')),
            ],
        ),
    ]
