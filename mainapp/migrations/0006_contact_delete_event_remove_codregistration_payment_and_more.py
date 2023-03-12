# Generated by Django 4.1.7 on 2023-03-12 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_valoregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('phone', models.CharField(blank=True, max_length=256, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.RemoveField(
            model_name='codregistration',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='fifaregistration',
            name='payment_image',
        ),
        migrations.RemoveField(
            model_name='valoregistration',
            name='payment',
        ),
    ]