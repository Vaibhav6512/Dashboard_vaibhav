# Generated by Django 3.1.4 on 2020-12-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_model', models.CharField(max_length=100)),
                ('secret_person', models.CharField(max_length=100)),
                ('friend_say', models.CharField(max_length=100)),
                ('question_ask', models.CharField(max_length=100)),
                ('nerver_say', models.CharField(max_length=100)),
                ('achievement', models.CharField(max_length=100)),
                ('failure', models.CharField(max_length=100)),
                ('learn_failure', models.CharField(max_length=100)),
                ('things_proud', models.CharField(max_length=100)),
                ('change_about', models.CharField(max_length=100)),
                ('first_things', models.CharField(max_length=100)),
                ('abstacle', models.CharField(max_length=100)),
                ('waste_time', models.CharField(max_length=100)),
                ('ritual', models.CharField(max_length=100)),
                ('favourite_place', models.CharField(max_length=100)),
                ('prefer', models.CharField(max_length=100)),
                ('happiest_period', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=100)),
                ('game', models.CharField(max_length=100)),
                ('injustice', models.CharField(max_length=100)),
                ('perfect_day', models.CharField(max_length=100)),
                ('take_time', models.CharField(max_length=100)),
                ('greatfull', models.CharField(max_length=100)),
                ('average_life', models.CharField(max_length=100)),
                ('marriage', models.CharField(max_length=100)),
                ('invent', models.CharField(max_length=100)),
                ('illegal', models.CharField(max_length=100)),
                ('discover', models.CharField(max_length=100)),
            ],
        ),
    ]
