# Generated by Django 5.1.3 on 2024-12-12 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_comments_blogcomment_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='parent',
        ),
    ]
