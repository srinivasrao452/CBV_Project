# Generated by Django 5.0.4 on 2024-04-10 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
                ('marks', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('mobile', models.BigIntegerField()),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
