# Generated by Django 3.1.4 on 2020-12-18 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Cadastro',
        ),
    ]
