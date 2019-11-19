# Generated by Django 2.2.6 on 2019-11-19 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20191120_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.User')),
                ('report_to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='mainapp.User')),
            ],
        ),
    ]
