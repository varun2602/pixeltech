# Generated by Django 4.1.1 on 2023-03-31 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_response', models.CharField(blank=True, default='timeout', max_length=100, null=True)),
                ('response_image', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
    ]
