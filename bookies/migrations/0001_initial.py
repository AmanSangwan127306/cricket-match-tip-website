# Generated by Django 3.0.7 on 2020-09-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(max_length=20000)),
                ('p2', models.CharField(max_length=20000)),
                ('p3', models.CharField(max_length=20000)),
            ],
        ),
    ]
