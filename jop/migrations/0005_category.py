# Generated by Django 4.0.4 on 2022-04-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0004_job_published_at_job_salary_job_vacancy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]