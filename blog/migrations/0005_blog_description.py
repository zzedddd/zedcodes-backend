# Generated by Django 4.1.4 on 2023-01-06 17:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.CharField(default='An Awesome Blog', max_length=256, validators=[django.core.validators.MinLengthValidator(10, 'description must be greater than 10 characters')]),
        ),
    ]
