# Generated by Django 3.1.1 on 2020-09-20 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empowerment', '0003_librarybook_bookpicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarybook',
            name='bookpicture',
            field=models.FileField(default='', upload_to='images/bookpicture'),
        ),
    ]