# Generated by Django 3.2.7 on 2021-10-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JigyasaApp', '0003_alter_leavereportstaff_leave_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackstaffs',
            name='feedback_reply',
            field=models.TextField(default=''),
        ),
    ]