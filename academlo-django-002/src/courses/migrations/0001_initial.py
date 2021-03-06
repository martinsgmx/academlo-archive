# Generated by Django 2.2.24 on 2021-06-27 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=256)),
                ('duration', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('url_image', models.CharField(max_length=128)),
                ('year', models.CharField(max_length=128)),
                ('is_activate', models.BooleanField(default=True)),
                ('students', models.ManyToManyField(related_name='course', to='students.Student')),
            ],
        ),
    ]
