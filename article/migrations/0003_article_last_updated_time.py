# Generated by Django 2.2.1 on 2019-07-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]