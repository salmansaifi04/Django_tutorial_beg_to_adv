# Generated by Django 4.0.6 on 2022-08-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_examcenter_myexamcenter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coaching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coachingname', models.CharField(max_length=100)),
                ('cityname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyCoaching',
            fields=[
            ],
            options={
                'ordering': ['cityname'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('school.coaching',),
        ),
    ]
