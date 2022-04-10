# Generated by Django 4.0.3 on 2022-03-26 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, verbose_name='Author')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('full_text', models.TextField(verbose_name='Text')),
                ('date', models.DateTimeField(verbose_name='Publish date')),
            ],
            options={
                'verbose_name': 'Posts',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
