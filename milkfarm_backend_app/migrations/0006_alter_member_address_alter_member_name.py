# Generated by Django 4.1.4 on 2023-05-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milkfarm_backend_app', '0005_auto_20230326_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]