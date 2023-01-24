# Generated by Django 4.1.4 on 2023-01-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0017_remove_scq_author_booleanques'),
    ]

    operations = [
        migrations.AddField(
            model_name='booleanques',
            name='marking',
            field=models.CharField(choices=[('nonegmarking', '+4/0'), ('negmarking', '+4/-1')], default='nonnegmarking', max_length=200),
        ),
    ]
