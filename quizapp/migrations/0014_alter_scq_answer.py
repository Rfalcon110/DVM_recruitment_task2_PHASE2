# Generated by Django 4.1.4 on 2023-01-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0013_alter_scq_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scq',
            name='answer',
            field=models.CharField(choices=[(1, 'choice 1'), (2, 'choice 2'), (3, 'choice 3'), (4, 'choice 4')], max_length=200),
        ),
    ]
