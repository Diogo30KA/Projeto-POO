# Generated by Django 4.2.2 on 2023-06-15 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.BigIntegerField(max_length=3)),
                ('cpf', models.BigIntegerField(max_length=11)),
            ],
        ),
    ]
