# Generated by Django 2.1.2 on 2018-10-22 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181022_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='fUser',
        ),
        migrations.AddField(
            model_name='comment',
            name='fUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
    ]
