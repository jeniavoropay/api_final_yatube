# Generated by Django 2.2.16 on 2022-12-04 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20221204_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('pub_date',)},
        ),
    ]
