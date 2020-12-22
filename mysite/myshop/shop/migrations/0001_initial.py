# Generated by Django 3.1.3 on 2020-11-23 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('patronymic', models.CharField(blank=True, max_length=45, null=True)),
                ('second_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('phone_number', models.IntegerField()),
                ('adress', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'clients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'collection',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=64)),
                ('size_xs', models.PositiveSmallIntegerField()),
                ('size_s', models.PositiveSmallIntegerField()),
                ('size_m', models.PositiveSmallIntegerField()),
                ('size_l', models.PositiveSmallIntegerField()),
                ('size_xl', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('number_of_sold', models.IntegerField()),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id_product', models.ForeignKey(db_column='id_product', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shop.products')),
                ('picture_number', models.IntegerField()),
                ('images', models.TextField()),
            ],
            options={
                'db_table': 'images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id_client', models.ForeignKey(db_column='id_client', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shop.clients')),
                ('id_order', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('size', models.IntegerField()),
                ('status', models.CharField(max_length=45)),
                ('data_of_issue', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
    ]