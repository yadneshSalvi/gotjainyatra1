# Generated by Django 2.2.2 on 2019-06-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dharamshala', '0013_auto_20190626_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='shala',
            name='ranking',
            field=models.IntegerField(default=1),
        ),
    ]
