# Generated by Django 5.0.1 on 2024-04-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_remove_user_insta_user_jobdescri1_user_jobdescri2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]