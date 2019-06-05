# Generated by Django 2.2 on 2019-05-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='caption2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
