# Generated by Django 3.0.5 on 2020-04-14 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_auto_20200413_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='name',
            field=models.TextField(default=''),
        ),
    ]