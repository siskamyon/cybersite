# Generated by Django 3.2.7 on 2024-05-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
