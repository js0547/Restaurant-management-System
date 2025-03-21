# Generated by Django 5.1.6 on 2025-03-03 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(db_column='Menu_ID', primary_key=True, serialize=False)),
                ('item_name', models.CharField(db_column='Item_Name', max_length=100)),
                ('price', models.DecimalField(db_column='Price', decimal_places=2, max_digits=10)),
                ('category', models.CharField(blank=True, choices=[('Appetizer', 'Appetizer'), ('Main Course', 'Main Course'), ('Dessert', 'Dessert'), ('Beverage', 'Beverage')], db_column='Category', max_length=20, null=True)),
                ('restaurant', models.ForeignKey(blank=True, db_column='Restaurant_ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
            options={
                'db_table': 'menu',
            },
        ),
    ]
