# Generated by Django 3.1.6 on 2021-02-11 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='question_content',
            new_name='question_description',
        ),
    ]
