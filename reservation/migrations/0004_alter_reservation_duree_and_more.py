# Generated by Django 5.2.2 on 2025-06-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20250626_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='duree',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='from_reserve',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='to_reserve',
            field=models.CharField(null=True),
        ),
    ]
