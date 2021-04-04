# Generated by Django 3.1.7 on 2021-03-31 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
            options={
                'db_table': 'botresponse',
            },
        ),
        migrations.CreateModel(
            name='Proker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'db_table': 'proker',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('event_type', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField()),
                ('proker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proker')),
            ],
            options={
                'db_table': 'event',
            },
        ),
    ]