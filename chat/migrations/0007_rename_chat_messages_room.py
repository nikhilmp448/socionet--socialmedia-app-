# Generated by Django 4.0 on 2022-09-29 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_rename_name_chats_room_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='Chat',
            new_name='room',
        ),
    ]
