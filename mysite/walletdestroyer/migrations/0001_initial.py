# Generated by Django 4.2.4 on 2023-10-10 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EarningModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('cost', models.PositiveIntegerField()),
                ('time_create', models.DateField()),
            ],
            options={
                'verbose_name': 'Earning',
                'ordering': ['-time_create'],
            },
        ),
        migrations.CreateModel(
            name='SpendingCategoriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SpendingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('cost', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True)),
                ('time_create', models.DateField()),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='walletdestroyer.spendingcategoriesmodel')),
            ],
            options={
                'verbose_name': 'Spending',
                'verbose_name_plural': 'Spending',
                'ordering': ['-time_create'],
            },
        ),
    ]
