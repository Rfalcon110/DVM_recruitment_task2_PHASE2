# Generated by Django 4.1.4 on 2023-01-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0019_intques_marking_scq_marking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='total',
            new_name='marks_scored',
        ),
        migrations.AddField(
            model_name='result',
            name='maximum_marks',
            field=models.IntegerField(default=0),
        ),
    ]
