# Generated by Django 3.2.4 on 2021-07-22 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_store_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'ordering': ['-id']},
        ),
    ]
