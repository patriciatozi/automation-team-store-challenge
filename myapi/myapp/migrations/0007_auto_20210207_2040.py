# Generated by Django 3.1.5 on 2021-02-07 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_csvimportdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('size', models.CharField(max_length=50)),
                ('style', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=15)),
                ('color', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=100)),
                ('post_date', models.DateField()),
                ('status', models.CharField(blank=True, choices=[('s', 'In Stock'), ('n', 'Non Available'), ('a', 'Available')], default='a', help_text='Shoe availability', max_length=1)),
            ],
            options={
                'db_table': 'table_shoes',
                'ordering': ['-post_date'],
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='CsvimportData',
        ),
    ]