# Generated by Django 5.1.6 on 2025-02-13 16:52

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='l_description',
            field=django_ckeditor_5.fields.CKEditor5Field(null=True),
        ),
    ]
