# Generated by Django 4.2.3 on 2023-09-23 15:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_subscriber'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscriber',
            new_name='Subscription',
        ),
    ]
