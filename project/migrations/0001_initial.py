# Generated by Django 5.1.5 on 2025-01-31 20:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', ckeditor.fields.RichTextField()),
                ('question_hi', models.TextField(blank=True, null=True)),
                ('question_bn', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
