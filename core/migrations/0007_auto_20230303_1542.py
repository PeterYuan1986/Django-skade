# Generated by Django 2.2.14 on 2023-03-03 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230303_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='noimg.jpg', upload_to=''),
        ),
    ]
