# Generated by Django 4.0.2 on 2022-04-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='Default.jpg', upload_to='media/images'),
        ),
    ]
