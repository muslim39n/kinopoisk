# Generated by Django 2.2.6 on 2019-12-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_watchlater'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/users'),
        ),
    ]
