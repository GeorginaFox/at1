# Generated by Django 5.0.1 on 2024-04-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduprod', '0003_delete_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(default='General', max_length=50),
        ),
    ]
