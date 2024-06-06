# Generated by Django 5.0.4 on 2024-06-05 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('is_private', models.BooleanField(default=False)),
                ('owner', models.CharField(max_length=255)),
            ],
        ),
    ]
