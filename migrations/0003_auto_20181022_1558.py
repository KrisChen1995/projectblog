# Generated by Django 2.1.2 on 2018-10-22 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_comment_fblog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='isDelte',
            new_name='isDelete',
        ),
    ]
