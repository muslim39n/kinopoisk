# Generated by Django 2.2.6 on 2019-11-26 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_auto_20191127_0016'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchLater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wl_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Movie')),
                ('wl_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.User')),
            ],
        ),
    ]
