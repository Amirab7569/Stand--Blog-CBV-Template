# Generated by Django 5.1.6 on 2025-03-02 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2025, 3, 2, 14, 40, 32, 426814, tzinfo=datetime.timezone.utc)),
        ),
    ]
