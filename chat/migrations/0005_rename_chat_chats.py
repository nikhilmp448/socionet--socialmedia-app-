# Generated by Django 4.0 on 2022-09-29 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_account_auth_provider_account_groups_and_more'),
        ('chat', '0004_chat_remove_messages_room_alter_messages_message_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chat',
            new_name='Chats',
        ),
    ]
