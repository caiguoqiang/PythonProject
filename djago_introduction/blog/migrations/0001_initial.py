# Generated by Django 3.1 on 2020-08-28 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('brief_content', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
