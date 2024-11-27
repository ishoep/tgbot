# Generated by Django 5.1.2 on 2024-10-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('event_id', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('hash_id', models.CharField(max_length=100)),
                ('hash_name', models.CharField(max_length=100)),
                ('source_id', models.CharField(max_length=100)),
                ('source_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_id', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('sub1', models.CharField(max_length=100)),
            ],
        ),
    ]
