# Generated by Django 2.2.6 on 2019-11-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20191106_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_url_image',
            field=models.CharField(default='mainapp\\images\\defaultuser.png', max_length=1000),
        ),
    ]
