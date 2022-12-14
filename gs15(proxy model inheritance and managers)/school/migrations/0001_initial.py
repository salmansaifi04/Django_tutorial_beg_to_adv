# Generated by Django 4.0.6 on 2022-08-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyExamCenter',
            fields=[
            ],
            options={
                'ordering': ['city'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('school.examcenter',),
        ),
    ]
