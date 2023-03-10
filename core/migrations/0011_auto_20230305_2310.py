# Generated by Django 2.2.14 on 2023-03-06 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20230303_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.TextField(default='Skade', max_length=10),
        ),
        migrations.AddField(
            model_name='item',
            name='img5',
            field=models.ImageField(default='noimg.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='img1',
            field=models.ImageField(default='noimg.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='img2',
            field=models.ImageField(default='noimg.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='img3',
            field=models.ImageField(default='noimg.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='img4',
            field=models.ImageField(default='noimg.jpg', upload_to=''),
        ),
    ]
