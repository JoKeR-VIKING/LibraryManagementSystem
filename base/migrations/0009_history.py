# Generated by Django 4.0.3 on 2022-04-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_student_assigned_books_student_max_assignable'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=100)),
                ('history', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]