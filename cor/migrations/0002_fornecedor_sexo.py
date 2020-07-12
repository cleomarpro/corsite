# Generated by Django 3.0.8 on 2020-07-08 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fornecedor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cor.Pessoa')),
                ('cnpj', models.CharField(max_length=20)),
            ],
            bases=('cor.pessoa',),
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=11)),
            ],
        ),
    ]