# Generated by Django 3.2.25 on 2024-03-23 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0009_alter_creditnote_reference_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditnote',
            name='reference_no',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
