# Generated by Django 2.2.2 on 2019-08-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190805_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='password'),
        ),
    ]
