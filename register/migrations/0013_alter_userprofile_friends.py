# Generated by Django 4.0.3 on 2022-03-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_alter_userprofile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='register.userprofile'),
        ),
    ]
