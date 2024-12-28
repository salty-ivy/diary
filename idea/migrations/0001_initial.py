# Generated by Django 5.1.4 on 2024-12-28 22:28

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0003_standardindexpage_standardpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaIndexPage',
            fields=[
                ('standardindexpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.standardindexpage')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('home.standardindexpage',),
        ),
        migrations.CreateModel(
            name='IdeaPage',
            fields=[
                ('standardpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.standardpage')),
            ],
            options={
                'abstract': False,
            },
            bases=('home.standardpage',),
        ),
    ]
