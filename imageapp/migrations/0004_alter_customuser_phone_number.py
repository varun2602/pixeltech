# Generated by Django 4.1.1 on 2023-03-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]