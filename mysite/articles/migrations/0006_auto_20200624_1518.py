# Generated by Django 3.0.7 on 2020-06-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='%y/%m/%d/'),
        ),
    ]