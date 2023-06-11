# Generated by Django 4.2.1 on 2023-06-11 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio/')),
            ],
        ),
    ]