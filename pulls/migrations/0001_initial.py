# Generated by Django 3.2.7 on 2021-10-21 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=20)),
                ('task_name', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('User_id', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='pulls.user')),
            ],
        ),
    ]
