# Generated by Django 3.1.1 on 2020-12-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surpriseapp', '0002_auto_20201216_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='overallView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_count', models.IntegerField(default=0)),
            ],
        ),
    ]
