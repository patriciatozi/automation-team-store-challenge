# Generated by Django 3.1.5 on 2021-02-07 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0005_delete_shoe'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvimportData',
            fields=[
                ('col_1', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('col_2', models.CharField(blank=True, default='', max_length=190)),
                ('col_3', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=6, null=True)),
                ('col_4', models.CharField(blank=True, default='', max_length=5)),
                ('col_5', models.CharField(blank=True, default='', max_length=9)),
                ('col_6', models.CharField(blank=True, default='', max_length=9)),
                ('col_7', models.CharField(blank=True, default='', max_length=42)),
                ('col_8', models.CharField(blank=True, default='', max_length=165)),
                ('col_9', models.DateTimeField(blank=True, null=True)),
                ('col_10', models.CharField(blank=True, default='', max_length=4)),
            ],
            options={
                'db_table': '"csvimport_data"',
                'managed': False,
            },
        ),
    ]
