# Generated by Django 4.2.1 on 2023-06-08 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_skills', models.CharField(max_length=50)),
                ('lvl_skills', models.IntegerField()),
            ],
        ),
    ]
