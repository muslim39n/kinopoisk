# Generated by Django 2.2.6 on 2019-11-12 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_user_user_url_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_role',
            field=models.CharField(default='user', max_length=32),
        ),
    ]
