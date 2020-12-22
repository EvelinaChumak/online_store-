# Generated by Django 3.1.3 on 2020-12-20 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id_client', models.ForeignKey(db_column='id_client', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='shop.users')),
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