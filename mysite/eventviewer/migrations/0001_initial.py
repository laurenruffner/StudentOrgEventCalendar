# Generated by Django 3.1.2 on 2020-10-28 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=200)),
                ('org_url', models.CharField(max_length=200)),
                ('org_description', models.CharField(max_length=200)),
                ('org_category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_datetime', models.DateTimeField(verbose_name='Start date and time of event')),
                ('event_description', models.CharField(max_length=200)),
                ('organizaiton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventviewer.organization')),
            ],
        ),
    ]