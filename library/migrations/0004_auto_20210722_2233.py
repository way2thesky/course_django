# Generated by Django 3.2.4 on 2021-07-22 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_store_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['-id']},
        ),
    ]
