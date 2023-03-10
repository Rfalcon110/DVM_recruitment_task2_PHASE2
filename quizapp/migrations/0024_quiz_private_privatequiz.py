# Generated by Django 4.1.4 on 2023-01-21 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0023_alter_mcq_choice_1_ans_alter_mcq_choice_2_ans_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='PrivateQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('quiz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizapp.quiz')),
            ],
        ),
    ]
