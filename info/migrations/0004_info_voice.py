# Generated by Django 4.0.4 on 2022-05-26 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_alter_info_name_alter_info_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='voice',
            field=models.FileField(default='incredible', upload_to=''),
            preserve_default=False,
        ),
    ]