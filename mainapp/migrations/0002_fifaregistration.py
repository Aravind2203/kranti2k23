# Generated by Django 4.1.7 on 2023-03-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FifaRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('team_name', models.CharField(blank=True, max_length=256, null=True)),
                ('college_name', models.CharField(blank=True, max_length=256, null=True)),
                ('member1', models.CharField(blank=True, max_length=256, null=True)),
                ('member2', models.CharField(blank=True, max_length=256, null=True)),
                ('phone1', models.CharField(blank=True, max_length=10, null=True)),
                ('phone2', models.CharField(blank=True, max_length=10, null=True)),
                ('event', models.CharField(blank=True, max_length=256, null=True)),
                ('year_of_study', models.PositiveIntegerField(blank=True, null=True)),
                ('payment_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
