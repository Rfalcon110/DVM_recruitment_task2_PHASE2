# Generated by Django 4.1.4 on 2023-01-19 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0016_intques'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scq',
            name='author',
        ),
        migrations.CreateModel(
            name='booleanques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, max_length=200, null=True)),
                ('answer', models.BooleanField()),
                ('quiz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizapp.quiz')),
            ],
        ),
    ]